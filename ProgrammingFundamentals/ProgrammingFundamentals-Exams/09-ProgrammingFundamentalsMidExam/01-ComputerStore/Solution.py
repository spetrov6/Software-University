command = input()
tax = 0
price_without_tax = 0
invalid_order = False
total_price = 0
while command != "special" and command != "regular":
    command = float(command)
    if command <= 0:
        print("Invalid price!")
    else:
        price_without_tax += command
        tax += command * 0.20
    command = input()
total_price = price_without_tax + tax
if price_without_tax == 0:
    print("Invalid order!")
    invalid_order = True
if not invalid_order:
    if command == "special":
        total_price -= total_price * 0.10
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_tax:.2f}$")
    print(f"Taxes: {tax:.2f}$""\n-----------")
    print(f"Total price: {total_price:.2f}$")