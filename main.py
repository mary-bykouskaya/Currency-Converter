amount_usd = [1, 1500, 25000]
amount_yuan = [1, 1750, 28000]
# Exchange rate USD to Yuan  = 6.74
USD_TO_YUAN = 6.74
# Exchange rate Yuan to USD = 0.148
YUAN_TO_USD = 0.148

for i in amount_usd:
    print(f"{i} USD to Yuan= {i * USD_TO_YUAN}")

for i in amount_yuan:
    print(f"{i} Yuan to USD = {i * YUAN_TO_USD}")

