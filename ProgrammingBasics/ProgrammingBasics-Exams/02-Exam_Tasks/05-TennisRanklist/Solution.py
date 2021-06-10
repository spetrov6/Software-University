from math import floor
tournaments_count = int(input())
points = int(input())
count = 0
points_after_start = 0
for i in range(tournaments_count):
    ranking = input()
    if ranking == "W":
        points += 2000
        points_after_start += 2000
        count += 1
    elif ranking == "F":
        points += 1200
        points_after_start += 1200
    elif ranking == "SF":
        points += 720
        points_after_start += 720
average = floor(points_after_start / tournaments_count )
print(f"Final points: {points}")
print(f"Average points: {average}")
print(f"{count / tournaments_count * 100:.2f}%")
