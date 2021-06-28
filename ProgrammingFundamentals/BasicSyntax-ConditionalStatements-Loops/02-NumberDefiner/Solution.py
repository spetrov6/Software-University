num = float(input())
if abs(num) < 1 and num != 0:
    print("small",end=" ")
elif abs(num) > 1000000:
    print("large",end=" ")
if num < 0:
    print("negative")
elif num > 0:
    print("positive")
elif num == 0:
    print("zero")
