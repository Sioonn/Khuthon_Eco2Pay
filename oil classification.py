import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 데이터셋 불러오기
df = pd.read_csv('./data/payment_history.csv')

# 주유소와 관련된 텍스트
gas_station_text = "주유소"

# 데이터셋에서 상호명 추출
business_names = df['상호명'].unique()

# TF-IDF 벡터화
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform([gas_station_text] + list(business_names))

# 상호명과 주유소와 관련된 텍스트 간의 코사인 유사도 계산
similarity_scores = cosine_similarity(X)

# 주유소와 유사한 상호명 출력
threshold = 0.5  # 임계값 설정
print("주유소와 유사한 상호명:")
for i, score in enumerate(similarity_scores[0][1:]):  # 첫 번째 요소는 주유소와 자기 자신의 유사도이므로 제외
    if score > threshold:
        print(f-"{business_names[i]} (유사도: {score:.2f})")