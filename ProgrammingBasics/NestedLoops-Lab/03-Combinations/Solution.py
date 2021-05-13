n = int(input())
count = 0
for x1 in range(101):
    for x2 in range(101):
        for x3 in range(101):
            if x1 + x2 + x3 == n:
               count += 1
print(count)