budget = float(input())
series_count = int(input())
budget_left = budget
for i in range(1, series_count +1):
    name = input()
    price = float(input())
    discount = 0
    if name == "Thrones":
        discount = price * 0.50
    elif name == "Lucifer":
        discount = price * 0.40
    elif name == "Protector":
        discount = price * 0.30
    elif name == "TotalDrama":
        discount = price * 0.20
    elif name == "Area":
        discount = price * 0.10
    budget_left = budget_left - (price - discount)
if budget_left >= 0:
    print(f"You bought all the series and left with {budget_left:.2f} lv.")
else:
    print(f"You need {abs(budget_left):.2f} lv. more to buy the series!")

