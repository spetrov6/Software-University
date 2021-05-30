n1 = int(input())
n2 = int(input())
magic_num = int(input())
combination_count = 0
equal = False
for first in range(n1, n2 + 1):
    for second in range(n1, n2 + 1):
        combination_count += 1
        if first + second == magic_num:
            print(f"Combination N:{combination_count} ({first} + {second} = {magic_num})")
            equal = True
            break
    if equal:
        break
if not equal:
    print(f"{combination_count} combinations - neither equals {magic_num}")

