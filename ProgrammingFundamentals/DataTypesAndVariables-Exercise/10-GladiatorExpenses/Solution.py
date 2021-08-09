from math import floor
loses = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expences = 0
count = 0
for i in range(1,loses + 1):
    if i % 2 == 0:
        total_expences += helmet_price
    if i % 3 == 0:
        total_expences += sword_price
    if i % 2 == 0 and i % 3 == 0:
        total_expences += shield_price
        count += 1
    if count == 2:
        total_expences += armor_price
        count = 0
print(f"Gladiator expenses: {total_expences:.2f} aureus")
