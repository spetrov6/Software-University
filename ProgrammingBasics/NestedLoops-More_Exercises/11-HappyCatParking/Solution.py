days = int(input())
hours = int(input())
total = 0
day_price = 0
for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 ==0 and hour % 2 != 0:
            total += 2.50
            day_price += 2.50
        elif day % 2 != 0 and hour %2 == 0:
            total += 1.25
            day_price += 1.25
        else:
            total += 1
            day_price += 1
    print(f"Day: {day} - {day_price:.2f} leva")
    day_price = 0
print(f"Total: {total:.2f} leva")