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

def main():
    try:
        cost = float(input("전기요금을 입력하세요 (원): "))
        if cost < 0:
            raise ValueError("음수의 전기요금은 입력할 수 없습니다.")

        usage, co2 = calculate_electricity_usage_and_co2_emission(cost)
        print("전기 사용량: {}kWh".format(usage))
        print("이산화탄소 배출량: {}kg".format(co2))
    except ValueError as ve:
        print("올바른 숫자를 입력하세요. ({})".format(ve))
    except Exception as e:
        print("오류가 발생했습니다. ({})".format(e))

if __name__ == "__main__":
    main()