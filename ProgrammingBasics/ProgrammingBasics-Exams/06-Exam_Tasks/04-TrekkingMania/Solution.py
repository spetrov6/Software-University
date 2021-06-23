groups_count = int(input())
musala = 0
monblant = 0
kilimandjaro = 0
k2 = 0
everest = 0
total_count = 0
for peoples in range(groups_count):
    peoples_count = int(input())
    if peoples_count <= 5:
        musala += peoples_count
    elif 6 <= peoples_count <= 12:
        monblant += peoples_count
    elif 13 <= peoples_count <= 25:
        kilimandjaro += peoples_count
    elif 26 <= peoples_count <= 40:
        k2 += peoples_count
    else:
        everest += peoples_count
    total_count += peoples_count
print(f"{musala / total_count * 100:.2f}%")
print(f"{monblant / total_count * 100:.2f}%")
print(f"{kilimandjaro / total_count * 100:.2f}%")
print(f"{k2 / total_count * 100:.2f}%")
print(f"{everest / total_count * 100:.2f}%")
