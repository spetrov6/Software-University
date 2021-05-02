from math import pi
form = input()
if form == "circle":
    side = float(input())
    s = pi * (side * side)
    print(f"{s:0.3f}")
elif form == "square":
    side = float(input())
    s = side * side
    print(f"{s:0.3f}")

elif form == "triangle":
     sideA = float(input())
     sideB = float(input())
     s = sideA * sideB / 2
     print(f"{s:0.3f}")
else:
    side1 = float(input())
    side2 = float(input())
    s = side1 * side2
    print(f"{s:0.3f}")