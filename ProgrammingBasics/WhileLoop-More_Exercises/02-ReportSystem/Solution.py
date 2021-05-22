needed_money = int(input())
command = input()
money_pos = 0
money_cash = 0
count = 0
person_cash = 0
person_pos = 0
total_money = 0
while command != "End":
    money = int(command)
    if count == 0:
        count += 1
        if money <= 100:
            person_cash += 1
            money_cash += money
            total_money += money
            print("Product sold!")
        elif money > 100:
            print("Error in transaction!")
    elif count == 1:
        count = 0
        if money > 10:
            person_pos += 1
            money_pos += money
            total_money += money
            print("Product sold!")
        elif money < 10:
            print("Error in transaction!")
    if total_money >= needed_money:
        print(f"Average CS: {money_cash / person_cash:.2f}")
        print(f"Average CC: {money_pos / person_pos:.2f}")
        break
    command = input()
if command == "End":
    print("Failed to collect required money for charity.")