budget = float(input())
ticket_type = input()
people_count = int(input())
transport = 0
budget_left = 0
if  1 <= people_count <= 4:
    transport = (budget * 0.75)
    if ticket_type == "VIP":
        budget_left = budget - transport - (people_count * 499.99)
    elif ticket_type == "Normal":
        budget_left = budget - transport - (people_count * 249.99)
elif  5 <= people_count <= 9:
    transport = (budget * 0.60)
    if ticket_type == "VIP":
        budget_left = budget - transport - (people_count * 499.99)
    else:
        budget_left = budget - transport - (people_count * 249.99)
elif  10 <= people_count <= 24:
    transport = (budget * 0.50)
    if ticket_type == "VIP":
        budget_left = budget - transport - (people_count * 499.99)
    else:
        budget_left = budget - transport - (people_count * 249.99)
elif  25 <= people_count <= 49:
    transport = (budget * 0.40)
    if ticket_type == "VIP":
        budget_left = budget - transport - (people_count * 499.99)
    else:
        budget_left = budget - transport - (people_count * 249.99)
elif  people_count >= 50:
    transport = (budget * 0.25)
    if ticket_type == "VIP":
        budget_left = budget - transport - (people_count * 499.99)
    else:
        budget_left = budget - transport - (people_count * 249.99)
if budget_left >= 0:
    print(f"Yes! You have {budget_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget_left):.2f} leva.")