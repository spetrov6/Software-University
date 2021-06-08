clients = int(input())
price = 0
total_price = 0
count = 0
for i in range(clients):
    type_desert = input()
    while type_desert != "Finish":
        if type_desert == "basket":
            price += 1.50
        elif type_desert == "wreath":
            price += 3.80
        else:
            price += 7
        count += 1
        type_desert = input()
    if count % 2 == 0:
        price -= price * 0.20
    print(f"You purchased {count} items for {price:.2f} leva.")
    total_price += price
    count = 0
    price = 0
print(f"Average bill per client is: {total_price / clients:.2f} leva.")
