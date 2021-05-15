num = int(input())
current = 1
bigger = False
for i in range(1, num + 1):
    for j in range(1, i + 1):
        if current > num:
            bigger = True
            break
        print(current, end=" ")
        current += 1
    print()
    if bigger:
        break