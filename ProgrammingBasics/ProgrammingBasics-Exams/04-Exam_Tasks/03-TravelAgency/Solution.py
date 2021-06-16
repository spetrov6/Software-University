town = input()
packet = input()
vip = input()
days = int(input())
price = 0
count = 0
if town == "Bansko" or town == "Borovets":
    if packet == "withEquipment":
        if vip == "yes":
            price = 90
        else:
            price = 100
    elif packet == "noEquipment":
        if vip == "yes":
            price = 76
        else:
            price = 80
    else:
        print("Invalid input!")
        count += 1
elif town == "Varna" or town == "Burgas":
    if packet == "withBreakfast":
        if vip == "yes":
            price = 114.40
        else:
            price = 130
    elif packet == "noBreakfast":
        if vip == "yes":
            price = 93
        else:
            price = 100
    else:
        print("Invalid input!")
        count += 1
else:
    print("Invalid input!")
    count += 1
if days < 1:
    print("Days must be positive number!")
    count +=1
elif days > 7:
    days -= 1
total_price = days * price
if count == 0:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")

