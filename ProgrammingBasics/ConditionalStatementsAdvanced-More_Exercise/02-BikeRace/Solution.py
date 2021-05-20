juniors = int(input())
seniors = int(input())
route = input()
total_racers = juniors + seniors
profit_juniors = 0
profit_seniors = 0
if route == "trail":
    profit_juniors = juniors * 5.50
    profit_seniors = seniors * 7
elif route == "cross-country":
    profit_juniors = juniors * 8
    profit_seniors = seniors * 9.50
elif route == "downhill":
    profit_juniors = juniors * 12.25
    profit_seniors = seniors * 13.75
else:
    profit_juniors = juniors * 20
    profit_seniors = seniors * 21.50
total_profit = profit_seniors + profit_juniors
if total_racers >= 50 and route == "cross-country":
    total_profit -= total_profit * 0.25
total_profit -= total_profit * 0.05
print(f"{total_profit:.2f}")
