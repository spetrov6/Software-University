eggs_size = input()
eggs_color = input()
lot = int(input())
price = 0
if eggs_size == "Large":
    if eggs_color == "Red":
        price = lot * 16
    elif eggs_color == "Green":
        price = lot * 12
    else:
        price = lot * 9
elif eggs_size == "Medium":
    if eggs_color == "Red":
        price = lot * 13
    elif eggs_color == "Green":
        price = lot * 9
    else:
        price = lot * 7
else:
    if eggs_color == "Red":
        price = lot * 9
    elif eggs_color == "Green":
        price = lot * 8
    else:
        price = lot * 5
profit = price - (price * 0.35)
print(f"{profit:.2f} leva.")