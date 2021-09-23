from collections import deque
rows,cols = [int(x) for x in input().split()]
snake = deque(input())
matrix = [["" for j in range(cols)]for x in range(rows)]
opposite_direction = False
for row in range(rows):
    if not opposite_direction:
        for col in range(cols):
            matrix[row][col] = snake[0]
            snake.append(snake.popleft())
        opposite_direction = True
    else:
        for col in range(cols - 1,-1,-1):
            matrix[row][col] = snake[0]
            snake.append(snake.popleft())
        opposite_direction = False
[print(''.join(x)) for x in matrix]
