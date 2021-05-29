n1 = int(input())
n2 = int(input())

for first in range(n1, n2 + 1):
    for second in range(n1, n2 + 1):
        for third in range(n1, n2 + 1):
            for fourth in range(n1, n2 + 1):
                sum1 = second + third
                if sum1 % 2 == 0 and first % 2 == 0 and fourth % 2 != 0 and first > fourth:
                    print(f"{first}{second}{third}{fourth}", end=" ")
                elif sum1 % 2 == 0 and first % 2 != 0 and fourth % 2 == 0 and first > fourth:
                    print(f"{first}{second}{third}{fourth}", end=" ")