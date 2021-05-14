n1 = int(input())
n2 = int(input())
magic_number = int(input())
count = 0
check = True
for num1 in range(n1, n2 + 1):
    if check:
        for num2 in range(n1, n2 + 1):
            count += 1
            if num1 + num2 == magic_number:
                print(f"Combination N:{count} ({num1} + {num2} = {magic_number})")
                check = False
                break
            elif num1 == n2 and num2 == n2:
                print(f"{count} combinations - neither equals {magic_number}")
    else:
        break
