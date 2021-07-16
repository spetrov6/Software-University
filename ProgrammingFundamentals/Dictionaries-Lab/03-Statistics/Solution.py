command = input()
products = {}
while command != "statistics":
    product = command.split(": ")[0]
    quantity = command.split(": ")[1]
    if product in products:
        products[product] = products[product] + int(quantity)
    else:
        products[product] = int(quantity)
    command = input()
print("Products in stock:")
for key,value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")