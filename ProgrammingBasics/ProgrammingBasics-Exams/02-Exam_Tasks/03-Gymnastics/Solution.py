country = input()
equipment = input()
difficulty = 0
performance = 0
rating = 0
if country == "Russia":
    if equipment == "ribbon":
        difficulty = 9.100
        performance = 9.400
    elif equipment == "hoop":
        difficulty = 9.300
        performance = 9.800
    else:
        difficulty = 9.600
        performance = 9.000
elif country == "Bulgaria":
    if equipment == "ribbon":
        difficulty = 9.600
        performance = 9.400
    elif equipment == "hoop":
        difficulty = 9.550
        performance = 9.750
    else:
        difficulty = 9.500
        performance = 9.400
else:
    if equipment == "ribbon":
        difficulty = 9.200
        performance = 9.500
    elif equipment == "hoop":
        difficulty = 9.450
        performance = 9.350
    else:
        difficulty = 9.700
        performance = 9.150
rating = difficulty + performance
insufficient = 20 - rating
print(f"The team of {country} get {rating:.3f} on {equipment}.")
print(f"{insufficient / 20 * 100:.2f}%")
