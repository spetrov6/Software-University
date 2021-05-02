num = float(input())
old_unit = input()
new_unit = input()

if old_unit == "m" and new_unit == "cm":
    num = num * 100
elif old_unit == "m" and new_unit == "mm":
    num = num * 1000
elif old_unit == "cm" and new_unit == "m":
    num = num / 100
elif old_unit == "cm" and new_unit == "mm":
    num = num * 10
elif old_unit == "mm" and new_unit == "m":
    num = num / 1000
else:
    num = num / 10

print(f"{num:0.3f}")