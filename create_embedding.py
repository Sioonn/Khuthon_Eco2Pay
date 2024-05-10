import numpy as np
import fasttext
import fasttext.util
# from sklearn.metrics.pairwise import cosine_similarity
def word_embedding(word_name):
    model_path = "word_embedding_model.bin"
    word_model = fasttext.load_model(model_path)
    return word_model.get_word_vector(word_name)

def create_embedding_vector(payment_institution):
    # payment_institution : String (ex : 부타센세)

    # 단어 임베딩 벡터를 저장할 리스트
    embedding_vectors = []

    # 단어의 임베딩 벡터를 가져와서 리스트에 추가
    embedding_vectors.append(word_embedding(payment_institution))

    # 리스트를 numpy 배열로 변환하여 반환
    # return : embedding vector tensor (ex : [[1.234234,2.235235,...], [0.453245345,2.245245, ...], ...])
    return np.array(embedding_vectors)
