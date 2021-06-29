num = input()
arr_digits = []
for digit in range(len(num)):
    arr_digits.append(num[digit])
arr_digits.sort(reverse=True)
arr_digits = "".join(arr_digits)
print(arr_digits)