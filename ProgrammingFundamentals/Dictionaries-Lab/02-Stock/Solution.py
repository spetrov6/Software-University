def check_product_and_quantity(searched,products_list):
    if searched in products_list:
        print(f"We have {products_list.get(searched)} of {searched} left")
    else:
        print(f"Sorry, we don't have {searched}")
products_as_string = input().split()
desired_products = input().split()
products = {}
for i in range(0,len(products_as_string),2):
    product = products_as_string[i]
    quantity = products_as_string[i + 1]
    products[product] = int(quantity)
for i in desired_products:
    check_product_and_quantity(i,products)