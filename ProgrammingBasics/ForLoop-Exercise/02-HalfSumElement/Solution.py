import sys
n = int(input())
biggest = -sys.maxsize
sum_number = 0
for i in range(0, n):
    num = int(input())
    if num > biggest:
        biggest = num
    sum_number += num

if biggest == sum_number - biggest:
    print("Yes"f"\nSum = {biggest}")
else:
    sum_other = abs(biggest - sum_number)
    print("No"f"\nDiff = {abs(biggest - sum_other)}")
