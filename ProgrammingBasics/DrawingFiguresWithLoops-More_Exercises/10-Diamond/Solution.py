from math import ceil
n = int(input())
left_right = int((n - 1) // 2)
mid = 0
if n % 2 == 0:
    for row in range(1, n):
        first_last = "-" * left_right + "**" + "-" * left_right
        line = "-" * left_right + "*" + "-" * mid + "*" + "-" * left_right
        if row == 1 or row == n:
            print(first_last)
            left_right -= 1
            mid += 2
        elif row < (n // 2):
            print(line)
            left_right -= 1
            mid += 2
        elif row == (n // 2):
            print(line)
            left_right += 1
            mid -= 2
        elif row > (n // 2):
            print(line)
            left_right += 1
            mid -= 2
else:
    for row in range(1,n + 1):
        first_last = "-" * left_right + "*" + "-" * left_right
        line = "-" * left_right + "*" + "-" * mid + "*" + "-" * left_right
        if row == 1 or row == n:
            print(first_last)
            left_right -= 1
            mid += 1
        elif row < ceil(n / 2):
            print(line)
            left_right -= 1
            mid += 2
        elif row == ceil(n / 2):
            print(line)
            left_right += 1
            mid -= 2
        elif row > ceil(n / 2):
            print(line)
            left_right += 1
            mid -= 2

