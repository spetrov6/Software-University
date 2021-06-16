drink = input()
sugar = input()
drinks_count = int(input())
price = 0
if drink == "Espresso":
    if sugar == "Without":
        price = 0.90
    elif sugar == "Normal":
        price = 1
    else:
        price = 1.20
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.20
    else:
        price = 1.60
else:
    if sugar == "Without":
        price = 0.50
    elif sugar == "Normal":
        price = 0.60
    else:
        price = 0.70
if sugar == "Without":
    price -= price * 0.35
if drink == "Espresso" and drinks_count >= 5:
    price -= price * 0.25
total_price = drinks_count * price
if total_price > 15:
    total_price -= total_price * 0.20
print(f"You bought {drinks_count} cups of {drink} for {total_price:.2f} lv.")
