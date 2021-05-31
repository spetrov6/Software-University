first = int(input())
second = int(input())
end_first = int(input())
end_second = int(input())
check1 = True
check2 = True
for num1 in range(first, first + end_first + 1):
    for num2 in range(second, second + end_second + 1):
        if num1 % 2 != 0 and num1 % 3 != 0 and num1 % 5 != 0 and num1 % 7 != 0 and num2 % 2 != 0 and num2 % 3 != 0 and num2 % 5 != 0 and num2 % 7 != 0:
            print(f"{num1}{num2}")




