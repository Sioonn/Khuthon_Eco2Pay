def heating_bill(payment, contract_area = 32): # 평수(계약면적)
    Mcal = (payment - contract_area*52.4) % 101.57
    return 0.123*Mcal