budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price =flour_price + (flour_price * 0.25)
colored_eggs = 0
price_cozonak = eggs_price + flour_price + (milk_price / 4)
cozonaks = 0
count = 0
while budget > price_cozonak:
    budget -= price_cozonak
    cozonaks += 1
    count += 1
    colored_eggs += 3
    if count == 3:
        colored_eggs -= cozonaks - 2
        count = 0
print(f"You made {cozonaks} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")





