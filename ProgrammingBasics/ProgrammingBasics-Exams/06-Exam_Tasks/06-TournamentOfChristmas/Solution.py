days = int(input())
win_count = 0
lose_count = 0
money = 0
win_days = 0
lose_days = 0
money_total = 0
for days in range(1,days + 1):
    sport = input()
    money = 0
    win_count = 0
    lose_count = 0
    while sport != "Finish":
        result = input()
        if result == "win":
            win_count += 1
            money += 20
        else:
            lose_count += 1
        sport = input()
    if win_count > lose_count:
        money_total += money + (money * 0.10)
        win_days += 1
    else:
        money_total += money
        lose_days += 1
if win_days > lose_days:
    money_total += money_total * 0.20
    print(f"You won the tournament! Total raised money: {money_total:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_total:.2f}")

