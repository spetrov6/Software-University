num = int(input())
if num <= 100:
    bonus = 5
elif num  > 100 and num <= 1000:
    bonus = num * 0.20
else:
    bonus = num * 0.10

if num % 2 == 0:
    bonus2 = 1
    print(bonus + bonus2)
    print(num + bonus + bonus2)
elif num % 10 == 5:
    bonus2 = 2
    print(bonus + bonus2)
    print(num + bonus + bonus2)
else:
    print(bonus)
    print(num + bonus)