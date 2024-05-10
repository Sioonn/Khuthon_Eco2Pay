# 1Mcal당0.123kgCO2

def Mcal_calculation(payment, contract_area):
    Mcal = (payment - contract_area*52.4) % 101.57
    return Mcal

def heating_bill(payment, contract_area = 32):
    return 0.123*Mcal_calculation(payment, contract_area) # 평수(계약면적)