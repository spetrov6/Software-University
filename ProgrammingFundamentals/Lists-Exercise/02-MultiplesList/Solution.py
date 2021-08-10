factor = int(input())
count = int(input())
number_list = []
num = 0
while len(number_list) != count:
    num += 1
    if num % factor == 0:
        number_list.append(num)
print(number_list)