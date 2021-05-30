n1 = int(input())
n2 = int(input())
n3 = int(input())
for first in range(1, n1 + 1):
    for second in range(1, n2 + 1):
        for third in range(1, n3 +1):
            if first % 2 ==0 and third % 2 == 0 and second != 4 and second != 6 and second <= 7 and second != 1:
                print(f"{first} {second} {third}")
