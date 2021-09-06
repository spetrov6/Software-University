number_of_names = int(input())
odd_set = set()
even_set = set()
current_row = 1
for _ in range(number_of_names):
    name = input()
    ascii_sum = sum([ord(x) for x in name]) // current_row
    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)
    current_row += 1
if sum(even_set) > sum(odd_set):
    print(', '.join([str(x) for x in odd_set.symmetric_difference(even_set)]))
elif sum(even_set) < sum(odd_set):
    print(', '.join([str(x) for x in odd_set.difference(even_set)]))
else:
    print(', '.join([str(x) for x in odd_set.union(even_set)]))
