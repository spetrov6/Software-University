stadion = int(input())
peoples = int(input())
A = 0
B = 0
V = 0
G = 0
for i in range(1, peoples + 1):
    sector = input()
    if sector == "A":
        A += 1
    elif sector == "B":
        B += 1
    elif sector == "V":
        V += 1
    elif sector == "G":
        G += 1
print(f"{A / peoples * 100:.2f}%")
print(f"{B / peoples * 100:.2f}%")
print(f"{V / peoples * 100:.2f}%")
print(f"{G / peoples * 100:.2f}%")
print(f"{peoples / stadion * 100:.2f}%")