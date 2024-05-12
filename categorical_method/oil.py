import pandas as pd

def calculate_co2_emission(price, fuel_type = '휘발유'):
    # payment_history.csv 파일을 불러와 데이터프레임으로 변환

    # 평균 연비
    average_mileage = 15.7

    # 휘발유와 경유의 가격 및 리터당 이산화탄소 배출량
    petrol_price_per_liter = 1715  # 경기 기준
    diesel_price_per_liter = 1557  # 경기 기준
    co2_per_liter = 2.4  # kg

   # 주어진 가격에 따라 휘발유와 경유의 판매량 계산
    if fuel_type == '휘발유':
        sales_volume = price / petrol_price_per_liter
    elif fuel_type == '경유':
        sales_volume = price / diesel_price_per_liter
    else:
        raise ValueError("유효하지 않은 연료 유형입니다.")

    # 이산화탄소 배출량 계산 (kg)
    co2_emission = sales_volume * co2_per_liter

    return co2_emission
# 사용자로부터 결제금액 입력 받기

