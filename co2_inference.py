from create_embedding import create_embedding_vector
import pandas as pd

file_path = './data/payment_history.csv'
data = pd.read_csv(file_path)

emb_vec_list = []
for i in range(len(data['상호명'])):
    payment_institution = data['상호명'][i]
    print(payment_institution)
    # embeded_vec = create_embedding_vector(payment_institution)
    # emb_vec_list.append(embeded_vec)



# for i in range(len())
# embeded_vec = create_embedding_vector()