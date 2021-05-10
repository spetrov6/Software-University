import sys
number = input()
num = -sys.maxsize
while number != "Stop":
    if int(number) > num:
        num = int(number)
    number = input()
print(num)