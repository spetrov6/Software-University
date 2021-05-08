import sys
n = int(input())
min = sys.maxsize
max = -sys.maxsize
for i in range(n):
    num = int(input())
    if num > max:
        max = num
    if num < min:
        min = num
print(f"Max number: {max}")
print(f"Min number: {min}")