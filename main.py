import datetime

amount_usd = [1, 1500, 25000]
amount_yuan = [1, 1750, 28000]
# Exchange rate USD to Yuan  = 6.74
USD_TO_YUAN = 6.74
# Exchange rate Yuan to USD = 0.148
YUAN_TO_USD = 0.148

current_date = datetime.datetime.now()
print("Current date: ", current_date.date())
print(f"Exchange rate USD to Yuan = {USD_TO_YUAN}")
print(f"Exchange rate Yuan to USD = {YUAN_TO_USD}")
print()

for i in amount_usd:
    print(f"{i} USD to Yuan= {i * USD_TO_YUAN}")
print()
for i in amount_yuan:
    print(f"{i} Yuan to USD = {i * YUAN_TO_USD}")

