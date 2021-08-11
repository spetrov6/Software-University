list_numbers = [int(i) for i in input().split(' ')]
num_remove = int(input())
lowest_list = []
for i in list_numbers:
    lowest_list.append(i)
lowest_list.sort()
for i in lowest_list[-1:num_remove - 1:-1]:
    lowest_list.remove(i)
for i in lowest_list:
    if i in list_numbers:
        list_numbers.remove(i)
print(list_numbers)