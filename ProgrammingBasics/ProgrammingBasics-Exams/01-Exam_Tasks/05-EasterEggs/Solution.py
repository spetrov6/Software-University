eggs_count = int(input())
blue = 0
red = 0
orange = 0
green = 0
for i in range(eggs_count):
    color = input()
    if color == "blue":
        blue += 1
    elif color == "red":
        red += 1
    elif color == "green":
        green += 1
    else:
        orange += 1
if red > orange and red > green and red >  blue:
    max_eggs = red
    max_color = "red"
elif blue > red and blue > green and blue > orange:
    max_eggs = blue
    max_color = "blue"
elif green > blue and green > red and green > orange:
    max_eggs = green
    max_color = "green"
else:
    max_eggs = orange
    max_color = "orange"
print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {max_color}")