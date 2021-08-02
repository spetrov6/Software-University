numbers_as_list = tuple([float(x) for x in input().split()])
numbers = sorted(set(numbers_as_list), key=numbers_as_list.index)
for x in numbers:
    print(f"{x} - {numbers_as_list.count(x)} times")