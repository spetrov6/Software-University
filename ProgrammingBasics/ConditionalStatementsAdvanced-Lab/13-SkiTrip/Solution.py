days = int(input()) - 1
room = input()
review = input()
if room == "room for one person":
    full_price = 18.00 * days
elif room == "apartment":
    full_price = 25.00 * days
else:
    full_price = 35.00 * days

if days < 10 and room == "apartment":
    discount = full_price * 0.30
elif days > 10 and days < 15 and room == "apartment":
    discount = full_price * 0.35
elif days > 15 and room == "apartment":
    discount = full_price / 2

elif days < 10 and room == "president apartment":
    discount = full_price * 0.10
elif days > 10 and days <15 and room == "president apartment":
    discount = full_price * 0.15
elif days > 15 and room == "president apartment":
    discount = full_price * 0.20
else:
    discount = 0

if review == "positive":
    discount_review = (full_price - discount) * 0.25
    price = full_price - discount + discount_review
    print(f"{price:0.2f}")
else:
    discount_review = (full_price - discount) * 0.10
    price = full_price - discount - discount_review
    print(f"{price:0.2f}")