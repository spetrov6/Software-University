money_needed = float(input())
money = float(input())
last_action = 0
days = 0
while money < money_needed:
    days += 1
    action = input()
    used_money = float(input())
    if action == "save":
        last_action = 0
        money += used_money
    elif action == "spend":
        money -= used_money
        last_action += 1
        if used_money > money:
            money = 0
        if last_action == 5:
            print(f"You can't save the money.\n{days}")
            break
if money >= money_needed:
    print(f"You saved the money for {days} days.")
