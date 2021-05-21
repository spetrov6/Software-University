season = input()
km_month = float(input())
km_season = km_month * 4
profit = 0
if km_month <= 5000:
    if season == "Spring" or season == "Autumn":
        profit = km_season * 0.75
    elif season == "Summer":
        profit = km_season * 0.90
    else:
        profit = km_season * 1.05
elif 5000 < km_month <= 10000:
    if season == "Spring" or season == "Autumn":
        profit = km_season * 0.95
    elif season == "Summer":
        profit = km_season * 1.10
    else:
        profit = km_season * 1.25
elif 10000 < km_month <= 20000:
    profit = km_season * 1.45
clear_profit = profit - (profit * 0.10)
print(f"{clear_profit:.2f}")
