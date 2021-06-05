guests = int(input())
price_person = float(input())
budget = float(input())
cake = budget * 0.10
total_price = 0
if 10 <= guests <= 15:
    price_person -= price_person * 0.15
    total_price = guests * price_person + cake
elif 16 <= guests <= 20:
    price_person -= price_person * 0.20
    total_price = guests * price_person + cake
elif guests >= 21:
    price_person -= price_person * 0.25
    total_price = guests * price_person + cake
else:
    total_price = guests * price_person + cake
if budget >= total_price:
    print(f"It is party time! {budget - total_price:.2f} leva left.")
else:
    print(f"No party! {total_price - budget:.2f} leva needed.")
