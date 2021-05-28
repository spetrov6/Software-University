l1 = ord(input())
l2 = ord(input())
l3 = ord(input())
count = 0
for first in range(l1, l2 + 1):
    for second in range(l1, l2 + 1):
        for third in range(l1, l2 + 1):
            if third != l3 and first != l3 and second != l3:
                count += 1
                print(f"{chr(first)}{chr(second)}{chr(third)}", end=" ")
print(count)