people_count = int(input())
invalid = 0
result = 0
zero = 0
ten = 0
twenty = 0
thirty = 0
fourty = 0
for i in range(1,people_count + 1):
    num = int(input())
    if num < 0 or num > 50:
        invalid += 1
        result = result / 2
    elif 0 <= num <= 9:
        zero += 1
        result += num * 0.20
    elif 10 <= num <= 19:
        ten += 1
        result += num * 0.30
    elif 20 <= num <= 29:
        twenty += 1
        result += num * 0.40
    elif 30 <= num <= 39:
        thirty += 1
        result += 50
    else:
        fourty += 1
        result += 100
print(f"{result:.2f}")
print(f"From 0 to 9: {zero / people_count * 100:.2f}%")
print(f"From 10 to 19: {ten / people_count * 100:.2f}%")
print(f"From 20 to 29: {twenty / people_count * 100:.2f}%")
print(f"From 30 to 39: {thirty / people_count * 100:.2f}%")
print(f"From 40 to 50: {fourty / people_count * 100:.2f}%")
print(f"Invalid numbers: {invalid / people_count * 100:.2f}%")