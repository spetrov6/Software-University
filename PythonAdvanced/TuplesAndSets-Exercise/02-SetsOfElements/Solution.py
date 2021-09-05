first_set_size,second_set_size = [int(x) for x in input().split()]
first_set = set([int(input()) for _ in range(first_set_size)])
second_set = set([int(input()) for _ in range(second_set_size)])
[print(x) for x in first_set.intersection(second_set)]
