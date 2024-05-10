from create_embedding import create_embedding_vector
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from oil import calculate_co2_emission

oil_type = '휘발유'
data = [
  {
    "상호명": "카페칸나",
    "시간": "19:08",
    "결제금액": -6100,
    "co2배출량": 0.50
  },
  {
    "상호명": "부타센세",
    "시간": "18:50",
    "결제금액": -8500,
    "co2배출량": 1.20
  },
  {
    "상호명": "하루텐동",
    "시간": "13:11",
    "결제금액": -11500,
    "co2배출량": 2.50
  },
  {
    "상호명": "한국전력공사",
    "시간": "9:12",
    "결제금액": -11258,
    "co2배출량": 22.40
  },
  {
    "상호명": "현대오일뱅크",
    "시간": "20:44",
    "결제금액": -50000,
    "co2배출량": 52.70
  },
  {
    "상호명": "musinsa",
    "시간": "21:10",
    "결제금액": -77560,
    "co2배출량": 12.80,
    "결제내역": "시티 레저 시어 윈드브레이커 외 3개"
  },
  {
    "상호명": "부대통령",
    "시간": "12:10",
    "결제금액": -7500,
    "co2배출량": 3.80
  },
  {
    "상호명": "지역난방",
    "시간": "7:02",
    "결제금액": -28802,
    "co2배출량": 88.70
  },
  {
    "상호명": "전광수커피하우",
    "시간": "14:20",
    "결제금액": -6600,
    "co2배출량": 1.10
  }
]

emb_vec_list = []
for i in range(len(data)):
    payment_institution = i['상호명']
    if payment_institution == '한국전력공사': 
        continue 
    elif payment_institution == '지역난방':
        continue
    emb_vec_list.append(create_embedding_vector(payment_institution))
    # embeded_vec = create_embedding_vector(payment_institution)
    # emb_vec_list.append(embeded_vec)
    embeded_vec = create_embedding_vector(payment_institution)
    emb_vec_list.append(embeded_vec)
