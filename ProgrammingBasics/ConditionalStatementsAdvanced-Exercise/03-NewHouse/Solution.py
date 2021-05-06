Flower = input()
Flower_count = int(input())
Budged = int(input())
price = 0
if Flower == "Roses":
    if Flower_count > 80:
        discount = (Flower_count * 5) * 0.10
        price = (Flower_count * 5) - discount
    else:
        price = Flower_count * 5
elif Flower == "Dahlias":
    if Flower_count > 90:
        discount = (Flower_count * 3.80) * 0.15
        price = (Flower_count * 3.80) - discount
    else:
        price = Flower_count * 3.80
elif Flower == "Tulips":
    if Flower_count > 80:
        discount = (Flower_count * 2.80) * 0.15
        price = (Flower_count * 2.80) - discount
    else:
        price = Flower_count * 2.80
elif Flower == "Narcissus":
    if Flower_count < 120:
        discount = (Flower_count * 3) * 0.15
        price = (Flower_count * 3) + discount
    else:
        price = Flower_count * 3
elif Flower == "Gladiolus":
    if Flower_count < 80:
        discount = (Flower_count * 2.50) * 0.20
        price = (Flower_count * 2.50) + discount
    else:
        price = Flower_count * 2.50


if Budged >= price:
    print(f"Hey, you have a great garden with {Flower_count} {Flower} and {Budged - price:0.2f} leva left.")
else:
    print(f"Not enough money, you need {price - Budged:0.2f} leva more.")