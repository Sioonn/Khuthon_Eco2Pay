from create_embedding import create_embedding_vector
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

file_path = './data/payment_history.csv'
data = pd.read_csv(file_path)

emb_vec_list = []
for i in range(len(data['상호명'])):
    payment_institution = data['상호명'][i]
<<<<<<< HEAD
    if payment_institution == '한국전력공사' or payment_institution == '지역난방':
        continue 
    emb_vec_list.append(create_embedding_vector(payment_institution))
    # embeded_vec = create_embedding_vector(payment_institution)
    # emb_vec_list.append(embeded_vec)
=======
    embeded_vec = create_embedding_vector(payment_institution)
    emb_vec_list.append(embeded_vec)
>>>>>>> 737334f9159162402a771fbd0cf1e094ff8bd7d7

classes = ['식당', '주유소', '옷']
embedded_classes = list(map(create_embedding_vector, classes))

# 각 emb_vec_list의 임베딩 벡터와 embedded_classes의 임베딩 벡터 간의 코사인 유사도 계산
similarities = []
for emb_vec in emb_vec_list:
    emb_similarities = [cosine_similarity([emb_vec], [embedded_class])[0][0] for embedded_class in embedded_classes]
    similarities.append(emb_similarities)

# 각 상호명에 대해 가장 유사한 클래스를 매핑
mapped_classes = []
for emb_similarities in similarities:
    max_similarity_index = emb_similarities.index(max(emb_similarities))
    mapped_class = classes[max_similarity_index]
    mapped_classes.append(mapped_class)

# 결과 출력
for i, mapped_class in enumerate(mapped_classes):
    print(f"상호명 '{data['상호명'][i]}'는 '{mapped_class}' 클래스와 가장 유사합니다.")