budget = float(input())
name = input()
budget_left = budget
salary = 0
total_salary = 0
while name != "ACTION":
    if len(name) <= 15:
        salary = float(input())
    elif len(name) > 15:
        salary = budget_left * 0.20
    budget_left -= salary
    total_salary += salary
    if budget_left < 0:
        print(f"We need {abs(budget_left):.2f} leva for our actors.")
        break
    salary = 0
    name = input()
if budget_left >= 0:
    print(f"We are left with {abs(budget_left):.2f} leva.")
