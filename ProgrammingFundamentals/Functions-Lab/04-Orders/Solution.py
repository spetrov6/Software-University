def order_price(product_type, quantity_of_product):
    store_dict = {"coffee":1.50, "water":1.00, "coke": 1.40, "snacks":2.00}
    if product_type in store_dict:
        return store_dict.get(product_type) * quantity_of_product
product = input()
quantity = int(input())
print(f"{order_price(product,quantity):.2f}")