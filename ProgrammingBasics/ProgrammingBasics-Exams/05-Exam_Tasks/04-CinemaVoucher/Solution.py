voucher = int(input())
product = input()
price = 0
money_left = voucher
tickets = 0
something = 0
while product != "End":
    if len(product) > 8:
        price = ord(product[0]) + ord(product[1])
        if price > money_left:
            break
        else:
            tickets += 1
    else:
        price = ord(product[0])
        if price > money_left:
            break
        else:
            something += 1
    money_left -= price
    product = input()
print(tickets)
print(something)

