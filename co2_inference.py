from create_embedding import create_embedding_vector
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

file_path = './data/payment_history.csv'
data = pd.read_csv(file_path)

emb_vec_list = []
for i in range(len(data['상호명'])):
    payment_institution = data['상호명'][i]
    if payment_institution == '한국전력공사' or payment_institution == '지역난방':
        continue 
    emb_vec_list.append(create_embedding_vector(payment_institution))
    # embeded_vec = create_embedding_vector(payment_institution)
    # emb_vec_list.append(embeded_vec)
    embeded_vec = create_embedding_vector(payment_institution)
    emb_vec_list.append(embeded_vec)
