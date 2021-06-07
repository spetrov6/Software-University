eggs = int(input())
amount = input()
count = 0
while amount != "Close":
    eggs_count = int(input())
    if amount == "Buy":
        if eggs_count > eggs:
            break
        else:
            eggs -= eggs_count
            count += eggs_count
    elif amount == "Fill":
        eggs += eggs_count
    amount = input()
if amount == "Close":
    print("Store is closed!")
    print(f"{count} eggs sold.")
else:
    print("Not enough eggs in store!")
    print(f"You can buy only {eggs}.")

