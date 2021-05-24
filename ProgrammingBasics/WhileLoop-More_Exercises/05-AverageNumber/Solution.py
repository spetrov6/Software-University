n = int(input())
count = 1
sum1 = 0
while count <= n:
    num = int(input())
    sum1 += num
    count += 1
print(f"{sum1 / n:.2f}")
