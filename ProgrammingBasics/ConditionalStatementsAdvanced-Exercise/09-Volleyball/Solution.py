year = input()
p = int(input())
h = int(input())
free_weekends = ((48 - h) / 4) * 3
holidays = (p / 3) * 2
games = free_weekends + h + holidays
if year == "leap":
    games = games + (games * 0.15)
print(int(games))