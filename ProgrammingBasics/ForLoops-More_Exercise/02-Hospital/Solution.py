days = int(input())
insuficient = 0
days_count = 0
doctors = 7
peoples = 0
for i in range(1, days + 1):
    days_count += 1
    if days_count == 3:
        days_count = 0
        if insuficient > peoples:
            doctors +=1
    people = int(input())
    if people > doctors:
        insuficient += (people - doctors)
        peoples += doctors
    else:
        peoples += people
print(f"Treated patients: {peoples}.")
print(f"Untreated patients: {insuficient}.")