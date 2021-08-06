amount = int(input())
days = int(input())
count = 0
spirit = 0
total_cost = 0
for i in range(1,days + 1):
    count += 1
    if count % 11 == 0:
        amount += 2
    if count % 2 == 0:
        total_cost += amount * 2
        spirit += 5
    if count % 3 == 0:
        total_cost += (amount * 5) + (amount * 3)
        spirit += 13
    if count % 3 == 0 and count % 5 == 0:
        total_cost += amount * 15
        spirit += 47
    elif count % 5 == 0:
        total_cost += amount * 15
        spirit += 17
    if count % 10 == 0:
        spirit -= 20
        total_cost += 5 + 3 + 15
        if i == days and i % 10 == 0:
            spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")
