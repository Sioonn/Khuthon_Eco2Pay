import os
import json

# 디렉토리 경로 설정
directory = 'C:/Users/LEECH/Desktop/data_project/222.관광 음식메뉴판 데이터/01-1.정식개방데이터/Validation/natural_data'

# 데이터를 저장할 리스트 생성
datas = []

# 디렉토리 내의 모든 파일에 대해 반복
for i,filename in enumerate(os.listdir(directory)):
    if i%100 == 0:
        print(i)
    # 파일 경로 생성
    filepath = os.path.join(directory, filename)
    
    # .json 파일인지 확인
    if filename.endswith('.json'):
        # 파일 열기
        with open(filepath, 'r', encoding='utf-8') as file:
            # JSON 데이터 읽기
            data = json.load(file)
            # 데이터를 리스트에 추가
            datas.append(data)

# 결과 확인
print(len(datas))

features = []
for store in datas:
    meta = store['meta']
    annotations = store['annotations']
    for annot in annotations:
        data = {}
        data['food_type'] = annot['menu_information']['food_type']
        data['food_subtype'] = annot['menu_information']['food_subtype']
        data['food_name'] = annot['menu_information']['ko']
        data['food_price'] = annot['menu_information']['price']
        data['ingred'] = annot['menu_information']['ingredients.ko']
        data['date'] = meta['captured_date'][0:4]
        data['store_type'] = meta['store_type']
        data['store_region'] = meta['store_region']
        features.append(data)

df = pd.DataFrame(features)
df