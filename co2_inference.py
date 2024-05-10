from create_embedding import create_embedding_vector
from oil import calculate_co2_emission
from carbon_footprint_regression import co2_per_clothes
from ingredient_prediction_model import MultiClassModel
from electric import calculate_electricity_usage_and_co2_emission
from hit import heating_bill

import torch
import re

# global var (회원가입 시 입력받는 variable)
oil_type = '휘발유'
contract_area = 32


data = [
  {
    "상호명": "카페칸나",
    "시간": "19:08",
    "결제금액": -6100,
  },
  {
    "상호명": "부타센세",
    "시간": "18:50",
    "결제금액": -8500,
  },
  {
    "상호명": "하루텐동",
    "시간": "13:11",
    "결제금액": -11500,
  },
  {
    "상호명": "한국전력공사",
    "시간": "9:12",
    "결제금액": -11258,
  },
  {
    "상호명": "현대오일뱅크",
    "시간": "20:44",
    "결제금액": -50000,
  },
  {
    "상호명": "musinsa",
    "시간": "21:10",
    "결제금액": -77560,
    "결제내역": "시티 레저 시어 윈드브레이커 외 3개"
  },
  {
    "상호명": "부대통령",
    "시간": "12:10",
    "결제금액": -7500
  },
  {
    "상호명": "지역난방",
    "시간": "7:02",
    "결제금액": -28802
  },
  {
    "상호명": "전광수커피하우스",
    "시간": "14:20",
    "결제금액": -6600
  }
]

co2_reduction_per_ingred = {
    "파": 6,
    "메밀면": 1,
    "어묵": 11,
    "새우": 12,
    "양파": 5,
    "탄산": 13,
    "춘장": 7,
    "쇠고기": 59,
    "치즈": 22,
    "생선": 6,
    "햄": 18,
    "버섯": 8,
    "마늘": 3,
    "된장": 9.3,
    "토마토": 1.4,
    "오징어": 8.6,
    "밀가루": 4.4,
    "면": 7,
    "낙지": 11.2,
    "음료": 15.5,
    "소시지": 14,
    "쌀": 4,
    "콩나물": 2.2,
    "김치": 7.8,
    "김": 5,
    "고기": 25,
    "두부": 3,
    "돼지고기": 12.31,
    "쌀": 4.45,
    "감자": 0.43,
    "계란": 4.67,
    "야채": 0.54,
    "치즈": 23.88,
    "새우": 26.86,
    "생선": 13.63,
    "닭고기": 9.86,
    "두부": 3.16,
    "토마토": 2.1,
    "파": 6,
    "어묵": 11,
    "양파": 5,
    "탄산": 13,
    "춘장": 7,
    "쇠고기": 59,
    "햄": 18,
    "버섯": 8,
    "마늘": 3,
    "된장": 9.3,
    "오징어": 8.6,
    "밀가루": 4.4,
    "면": 7,
    "낙지": 11.2,
    "음료": 15.5,
    "소시지": 14,
    "콩나물": 2.2,
    "김치": 7.8,
    "김": 5,
    "고기": 25
}

for item in data:
    item["결제금액"] *= -1

items_str = "돼지고기,누룩,숙주,계란,참치,떡,야채,당면,고추장,소고기,해물,전복,전분,보리,해산물,고추,육수,알코올,채소,닭고기,파스타면,감자,연어,파,메밀면,어묵,새우,양파,탄산,춘장,쇠고기,치즈,생선,햄,버섯,마늘,두부,된장,토마토,오징어,밀가루,면,낙지,음료,소시지,쌀,콩나물,김치,김,고기"

ingred_list = items_str.split(',')


emb_vec_list = []
pattern = re.compile(r'주유|주유소|S-OIL|오일|오일뱅크|현대오일뱅크')

def find_max_index(tensor):
  # 텐서의 최댓값과 해당 인덱스를 반환합니다.
  max_value, max_index = torch.max(tensor, dim=1)
  return max_index.item()  # 최댓값의 인덱스를 반환합니다.


for i in data:
  payment_institution = i['상호명']
  if payment_institution == '한국전력공사': 
      _,result = calculate_electricity_usage_and_co2_emission(i['결제금액']) 
  elif payment_institution == '지역난방':
      result = heating_bill(i['결제금액'], contract_area)
  elif re.search(pattern, payment_institution):
      result = calculate_co2_emission(i['결제금액'], oil_type)
  elif payment_institution == 'musinsa':
      clothes_num = int(i['결제내역'][-2]) + 1
      result = co2_per_clothes(clothes_num)
  else:
      embeded_vec = create_embedding_vector(payment_institution)
      ingred_tensor_input = torch.FloatTensor(embeded_vec)
      ingred_model = MultiClassModel(300, 50)
      ingred_checkpoint = torch.load('model/ingredient_prediction_model.pth')
      ingred_model.load_state_dict(ingred_checkpoint['model_state_dict'])

      ingred_model.eval()
      with torch.no_grad():
        output = ingred_model(ingred_tensor_input)
    
      max_index = find_max_index(output)
      result = co2_reduction_per_ingred[ingred_list[max_index]]
    
  i["CO2 배출량"] = result
  print(result)
    # embeded_vec = create_embedding_vector(payment_institution)
    # emb_vec_list.append(embeded_vec)
    
print(data)