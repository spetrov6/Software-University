flour_price = float(input())
flour_amount = float(input())
sugar_amount = float(input())
eggs_amount = int(input())
yeast_amount = int(input())
sugar_price = flour_price - (flour_price * 0.25)
eggs_price = flour_price + (flour_price * 0.10)
yeast_price = sugar_price - (sugar_price * 0.80)
flour_total = flour_amount * flour_price
eggs_total = eggs_amount * eggs_price
yeast_total = yeast_amount * yeast_price
sugar_total = sugar_amount * sugar_price
total = flour_total + yeast_total + sugar_total + eggs_total
print(f"{total:.2f}")