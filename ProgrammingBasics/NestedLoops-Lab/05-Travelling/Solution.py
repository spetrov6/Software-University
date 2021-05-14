destination = input()
while destination != "End":
    money_needed = float(input())
    while money_needed > 0:
        money_save = float(input())
        money_needed -= money_save
        if money_needed <= 0:
            print(f"Going to {destination}!")
    destination = input()