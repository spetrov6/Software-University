n_km = int(input())
time_day = input()
money = 0
if n_km >= 100:
    money = n_km * 0.06
elif 20 <= n_km < 100:
    money = n_km * 0.09
else:
    if time_day == "day":
        money = 0.70 + (n_km * 0.79)
    else:
        money = 0.70 + (n_km * 0.90)
print(f"{money:.2f}")