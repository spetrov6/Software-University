destination = input()
dates = input()
nights = int(input())
price = 0
if dates == "21-23":
    if destination == "France":
        price = nights * 30
    elif destination == "Italy":
        price = nights * 28
    else:
        price = nights * 32
elif dates == "24-27":
    if destination == "France":
        price = nights * 35
    elif destination == "Italy":
        price = nights * 32
    else:
        price = nights * 37
else:
    if destination == "France":
        price = nights * 40
    elif destination == "Italy":
        price = nights * 39
    else:
        price = nights * 43
print(f"Easter trip to {destination} : {price:.2f} leva.")