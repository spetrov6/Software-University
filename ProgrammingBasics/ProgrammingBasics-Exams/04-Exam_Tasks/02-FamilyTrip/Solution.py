budget = float(input())
nights = int(input())
night_price = float(input())
expences_percent = int(input()) * 0.01
if nights > 7:
    night_price -= night_price * 0.05
price = nights * night_price
budget_left = budget - (budget * expences_percent)
if budget_left >= price:
    print(f"Ivanovi will be left with {budget_left - price:.2f} leva after vacation.")
else:
    print(f"{price - budget_left:.2f} leva needed.")