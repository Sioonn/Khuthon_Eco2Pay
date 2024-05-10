def calculate_electricity_usage_and_co2_emission(cost):
    """
    전기요금에 따른 전기 사용량과 이산화탄소 배출량을 계산하는 함수
    :param cost: 전기요금 (원)
    :return: 전기 사용량 (kWh), 이산화탄소 배출량 (kg)
    """
    if cost <= 36000:  # 300kWh * 120원
        usage = cost / 120
    elif 36000 < cost <= 96300:  # 450kWh * 214원
        usage = 300 + (cost - 36000) / 214
    else:
        usage = 450 + (cost - 96300) / 307

    co2_emission = usage * 4.77  # 1kWh당 4.77kg의 이산화탄소 배출

    return usage, co2_emission
