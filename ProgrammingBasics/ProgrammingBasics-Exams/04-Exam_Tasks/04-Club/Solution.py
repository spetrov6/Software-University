desired_profit = float(input())
coctail = input()
profit = 0
while coctail != "Party!":
    coctails_count = int(input())
    price = len(coctail)
    order = price * coctails_count
    if order % 2 != 0:
        order -= order * 0.25
    profit += order
    if profit >= desired_profit:
        break
    coctail = input()
if profit < desired_profit:
    print(f"We need {desired_profit - profit:.2f} leva more.")
else:
    print("Target acquired.")
print(f"Club income - {profit:.2f} leva.")
