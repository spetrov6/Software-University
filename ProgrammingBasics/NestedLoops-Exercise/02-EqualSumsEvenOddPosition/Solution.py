num1 = int(input()) #100000
num2 = int(input()) #100050
count = 1
for i in range(num1, num2 + 1):
    num = str(i)
    even_sum = 0
    odd_sum = 0
    for j in num:
        if count % 2 == 0:
            even_sum += int(j)
        else:
            odd_sum += int(j)
        count += 1
    if even_sum == odd_sum:
        print(i, end=" ")


