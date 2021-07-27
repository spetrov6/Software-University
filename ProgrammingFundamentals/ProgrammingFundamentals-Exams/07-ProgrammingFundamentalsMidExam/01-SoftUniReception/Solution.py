first_employ = int(input())
second_employ = int(input())
third_employ = int(input())
students = int(input())
answers_per_hour = first_employ + second_employ + third_employ
count = 1
hours = 0
while students > 0:
    if count % 4 == 0:
        hours += 1
    else:
        students -= answers_per_hour
        hours += 1
    count += 1
print(f"Time needed: {hours}h.")