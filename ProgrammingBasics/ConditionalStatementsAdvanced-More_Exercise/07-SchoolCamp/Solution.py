season = input()
group_type = input()
kids_count = int(input())
nights = int(input())
if season == "Winter":
    if group_type == "boys" or group_type == "girls":
        if group_type == "boys":
            sport = "Judo"
        elif group_type == "girls":
            sport = "Gymnastics"
        price = (nights * 9.60) * kids_count
    else:
        price = (nights * 10) * kids_count
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys" or group_type == "girls":
        if group_type == "boys":
            sport = "Tennis"
        elif group_type == "girls":
            sport = "Athletics"
        price = (nights * 7.20) * kids_count
    else:
        price = (nights * 9.50) * kids_count
        sport = "Cycling"
else:
    if group_type == "boys" or group_type == "girls":
        if group_type == "boys":
            sport = "Football"
        elif group_type == "girls":
            sport = "Volleyball"
        price = (nights * 15) * kids_count
    else:
        price = (nights * 20) * kids_count
        sport = "Swimming"
if kids_count >= 50:
    price -= price * 0.50
elif 20 <= kids_count < 50:
    price -= price  * 0.15
elif 10 <= kids_count < 20:
    price -= price * 0.05
print(f"{sport} {price:.2f} lv.")