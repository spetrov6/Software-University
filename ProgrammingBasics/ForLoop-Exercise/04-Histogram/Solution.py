n = int(input())
p1 = []
p2 = []
p3 = []
p4 = []
p5 = []

for i in range(n):
    num = int(input())
    if num < 200:
        p1.append(num)
    elif 200 <= num <= 399:
        p2.append(num)
    elif 400 <= num <= 599:
        p3.append(num)
    elif 600 <= num <= 799:
        p4.append(num)
    elif num >= 800:
        p5.append(num)
print(f"{(len(p1) / n) * 100:.2f}%")
print(f"{(len(p2) / n) * 100:.2f}%")
print(f"{(len(p3) / n) * 100:.2f}%")
print(f"{(len(p4) / n) * 100:.2f}%")
print(f"{(len(p5) / n) * 100:.2f}%")


