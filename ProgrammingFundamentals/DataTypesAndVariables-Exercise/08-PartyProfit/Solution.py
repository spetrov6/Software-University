from math import floor
group = int(input())
days = int(input())
coin = days * 50
for i in range(1, days + 1):
    if i % 10 == 0:
        group -= 2
    if i % 15 == 0:
        group += 5
    coin -= group * 2
    if i % 3 == 0 and i % 5 == 0:
        coin += group * 20
        coin -= group * 5
    elif i % 3 == 0:
        coin -= group * 3
    elif i % 5 == 0:
        coin += group * 20
print(f"{group} companions received {floor(coin / group)} coins each.")
