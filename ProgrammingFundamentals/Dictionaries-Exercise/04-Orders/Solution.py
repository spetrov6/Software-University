total_products_price = {}
products_prices = {}
products_quantity = {}
products_as_string = input()
while products_as_string != "buy":
    product,price,quantity = products_as_string.split()
    products_prices[product] = float(price)
    if product in products_quantity:
        products_quantity[product] += float(quantity)
    else:
        products_quantity[product] = float(quantity)
    products_as_string = input()
for i in products_quantity:
    total_products_price[i] = products_quantity[i] * products_prices[i]
for key,value in total_products_price.items():
    print(f"{key} -> {value:.2f}")