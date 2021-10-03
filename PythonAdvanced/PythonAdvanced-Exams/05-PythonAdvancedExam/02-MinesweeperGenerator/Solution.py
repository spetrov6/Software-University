from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = deque([int(x) for x in input().split(", ")])
size_of_matrix = int(input())
bombs_count = int(input())
matrix = [["0" for _ in range(size_of_matrix)] for _ in range(size_of_matrix)]
near_bombs_count = 0
next_positions = [(-1, 0), (+1, 0), (0, -1), (0, +1), (-1, -1), (-1, +1), (+1, -1), (+1, +1)]

for _ in range(bombs_count):
    [row, col] = map(lambda x: int(x), input()[1:][:-1].split(', '))
    matrix[row][col] = '*'

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] != "*":
            for position in next_positions:
                next_row = row + position[0]
                next_col = col + position[1]
                if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix):
                    if matrix[next_row][next_col] == "*":
                        near_bombs_count += 1
            matrix[row][col] = str(near_bombs_count)
            near_bombs_count = 0
[print(' '.join(x)) for x in matrix]
total_time_passed = 0

while True:
    if len(customers) > 0:
        if len(taxis) > 0:
            if taxis[-1] >= customers[0]:
                total_time_passed += customers[0]
                taxis.pop()
                customers.popleft()
            else:
                taxis.pop()
        else:
            print("Not all customers were driven to their destinations")
            print(f"Customers left: {', '.join([str(x) for x in customers])}")
            break
    else:
        print("All customers were driven to their destinations")
        print(f"Total time: {total_time_passed} minutes")
        break

