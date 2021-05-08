n = int(input())
result1 = 0
result2 = 0
for i in range(n):
    num = int(input())
    result1 += num
for i in range(n):
    num = int(input())
    result2 += num
if result1 == result2:
    print(f"Yes, sum = {abs(result2)}")
else:
    print(f"No, diff = {abs(result2 - result1)}")
