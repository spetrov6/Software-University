from math import ceil
peoples_count = int(input())
elevator_space = int(input())
up_down = peoples_count / elevator_space
print(ceil(up_down))