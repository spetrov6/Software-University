from math import ceil
height = int(input())
width = int(input())
occupied = int(input()) * 0.01
wall = height * width
area_total = (wall * 4)
area = ceil(area_total - (area_total * occupied))
command = input()
while command != "Tired!":
    paint = int(command)
    area -= paint
    if area <= 0:
        break
    command = input()
if area > 0:
    print(f"{area} quadratic m left.")
elif area < 0:
    print(f"All walls are painted and you have {abs(area)} l paint left!")
else:
    print("All walls are painted! Great job, Pesho!")
