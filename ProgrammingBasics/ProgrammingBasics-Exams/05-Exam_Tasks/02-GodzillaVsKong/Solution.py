budget = float(input())
staff = int(input())
clothes = float(input())
deckour = budget * 0.10
clothes_price = staff * clothes
if staff > 150:
    clothes_price -= clothes_price * 0.10
total = clothes_price + deckour
if budget >= total:
    print("Action!")
    print(f"Wingard starts filming with {budget - total:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total - budget:.2f} leva more.")