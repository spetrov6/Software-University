n = int(input())
even = 0
odd = 0
num = 0
for i in range(n):
    num = int(input())
    if i % 2 ==0:
        even += num
    else:
        odd += num
if even == odd:
    print("Yes"f"\nSum = {even}")
else:
    print("No"f"\nDiff = {abs(even - odd)}")
