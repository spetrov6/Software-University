numbers = input()
numbers_list = numbers.split(sep=" ")
numbers_reversed = []
for i in numbers_list:
    num = int(i)
    if num < 0:
        numbers_reversed.append(abs(num))
    else:
        numbers_reversed.append(-abs(num))
print(numbers_reversed)