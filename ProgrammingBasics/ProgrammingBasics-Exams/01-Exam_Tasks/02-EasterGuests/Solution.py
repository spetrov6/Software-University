from math import ceil
guests = int(input())
budged = int(input())
bread = ceil(guests / 3)
bread_price = bread * 4
eggs = guests * 2
eggs_price = eggs * 0.45
total = bread_price + eggs_price
if budged >= total:
    print(f"Lyubo bought {bread} Easter bread and {eggs} eggs.")
    print(f"He has {budged - total:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {total - budged:.2f} lv. more.")
