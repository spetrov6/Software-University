item_price = input().split("|")
budget = float(input())
new_price = []
profit = 0
for index in range(len(item_price)):
    item_price[index] = item_price[index].split("->")
    price = float(item_price[index][1])
    item = item_price[index][0]
    if price <= budget:
        if item == "Clothes" and price <= 50.00:
            budget -= price
            profit += price * 0.40
            new_price.append(price + price * 0.40)
        elif item == "Shoes" and price <= 35.00:
            budget -= price
            profit += price * 0.40
            new_price.append(price + price * 0.40)
        elif item == "Accessories" and price <= 20.50:
            budget -= price
            profit += price * 0.40
            new_price.append(price + price * 0.40)
for i in new_price:
    budget += i
    print(f"{i:.2f}",end=" ")
print(f"\nProfit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")


