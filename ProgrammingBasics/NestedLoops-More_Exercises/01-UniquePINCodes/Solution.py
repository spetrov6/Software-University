n1 = int(input())
n2 = int(input())
n3 = int(input())
for dig1 in range(1, n1 + 1):
    for dig2 in range(2, n2 + 1):
        for dig3 in range(1,n3 + 1):
            if dig1 % 2 == 0 and dig3 % 2 == 0 and dig2 != 4 and dig2 != 6 and dig2 != 8 and dig2 != 9:
                print(f"{dig1} {dig2} {dig3}")