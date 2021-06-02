n = int(input())
for sideA in range(1,n + 1):
    if sideA == 1 or sideA == n:
        print("+", end=" ")
    else:
        print("|", end=" ")
    for sideB in range(1,n + 1):
        if sideA == 1 and sideB == n or sideA == n and sideB == n:
            print("+", end=" ")
        elif sideA != 1 and sideB == n:
            print("|", end=" ")
        elif 1 < sideB < n:
            print("-", end=" ")
    print()

