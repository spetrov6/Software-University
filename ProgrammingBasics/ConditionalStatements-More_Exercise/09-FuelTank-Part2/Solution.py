fuel = input()
fuel_amount = float(input())
card = input()
price = 0
if fuel == "Gas":
    total_price = fuel_amount * 0.93
    if card == "Yes":
        discount = fuel_amount * 0.08
        total_price = total_price - discount
    if 20 <= fuel_amount <= 25:
        discount2 = total_price * 0.08
        total_price -= discount2
    elif fuel_amount > 25:
        discount2 = total_price * 0.10
        total_price -= discount2
elif fuel == "Gasoline":
    total_price = fuel_amount * 2.22
    if card == "Yes":
        discount = fuel_amount * 0.18
        total_price = total_price - discount
    if 20 <= fuel_amount <= 25:
        discount2 = total_price * 0.08
        total_price -= discount2
    elif fuel_amount > 25:
        discount2 = total_price * 0.10
        total_price -= discount2
elif fuel == "Diesel":
    total_price = fuel_amount * 2.33
    if card == "Yes":
        discount = fuel_amount * 0.12
        total_price = total_price - discount
    if 20 <= fuel_amount <= 25:
        discount2 = total_price * 0.08
        total_price -= discount2
    elif fuel_amount > 25:
        discount2 = total_price * 0.10
        total_price -= discount2
print(f"{total_price:.2f} lv.")




