movie_budget = float(input())
place = input()
season = input()
days = int(input())
value = 0
if place == "Dubai":
    if season == "Winter":
        value = 45000
    else:
        value = 40000
elif place == "Sofia":
    if season == "Winter":
        value = 17000
    else:
        value = 12500
else:
    if season == "Winter":
        value = 24000
    else:
        value = 20250
total_value = value * days
if place == "Sofia":
    total_value += (total_value * 0.25)
elif place == "Dubai":
    total_value -= (total_value * 0.30)
if movie_budget >= total_value:
    print(f"The budget for the movie is enough! We have {movie_budget - total_value:.2f} leva left!")
else:
    print(f"The director needs {total_value - movie_budget:.2f} leva more!")
