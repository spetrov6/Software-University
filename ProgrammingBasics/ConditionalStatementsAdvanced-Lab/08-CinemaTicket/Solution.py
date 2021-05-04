day = input()
price_day = {"Monday":12, "Tuesday":12, "Friday":12, "Wednesday":14, "Thursday":14, "Saturday":16, "Sunday":16}
for key,value in price_day.items():
    if day == key:
        print(value)