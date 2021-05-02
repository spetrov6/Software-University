budget = float(input())
extra = int(input())
clothes_price = float(input()) * extra
if extra > 150:
    clothes_price = clothes_price - (clothes_price * 0.10)
decor = budget * 0.10
costs = decor + clothes_price
if budget >= costs:
   print("Action!")
   print(f"Wingard starts filming with {budget - costs:0.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {costs - budget:0.2f} leva more.")