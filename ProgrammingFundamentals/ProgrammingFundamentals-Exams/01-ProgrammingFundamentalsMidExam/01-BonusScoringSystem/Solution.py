from math import ceil
students_count = int(input())
lectures_count = int(input())
initial_bonus = int(input())
max_bonus = 0
max_attendances = 0
bonus = 0
for _ in range(students_count):
    attendances = int(input())
    bonus = attendances / lectures_count * (5 + initial_bonus)
    if bonus > max_bonus:
        max_bonus = bonus
        max_attendances = attendances
print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")