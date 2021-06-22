fruit = input()
set_type = input()
set_count = int(input())
discount = 0
if set_type == "small":
    if fruit == "Watermelon":
        total = set_count * 2 * 56
    elif fruit == "Mango":
        total = set_count * 2 * 36.66
    elif fruit == "Pineapple":
        total = set_count * 2 * 42.10
    else:
        total = set_count * 2 * 20
else:
    if fruit == "Watermelon":
        total = set_count * 5 * 28.70
    elif fruit == "Mango":
        total = set_count * 5 * 19.60
    elif fruit == "Pineapple":
        total = set_count * 5 * 24.80
    else:
        total = set_count * 5 * 15.20
if 400 <= total <= 1000:
    discount = total * 0.15
elif total > 1000:
    discount = total / 2
print(f"{total - discount:.2f} lv.")
