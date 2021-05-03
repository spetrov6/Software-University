day = int(input())
days = ["Error", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if day >= 1 and day <= 7:
    print(days[day])
else:
    print(days[0])