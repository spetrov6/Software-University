def initial_snake_and_burrows_positions():
    burrows = []
    snake = tuple()
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "S":
                snake = (row, col)
            elif matrix[row][col] == "B":
                burrows.append((row, col))
    return snake, burrows


def valid_next_position():
    if 0 <= snake_next_position[0] < len(matrix)\
            and 0 <= snake_next_position[1] < len(matrix):
        return True
    return False


def matrix_arrange():
    matrix[snake_next_position[0]][snake_next_position[1]] = "S"
    matrix[snake_position[0]][snake_position[1]] = "."


snake_moves = {"up": (-1, 0), "left": (0, -1), "right": (0, +1), "down": (+1, 0)}
size_of_matrix = int(input())
matrix = [[x for x in input()] for _ in range(size_of_matrix)]
snake_position, burrows_positions = initial_snake_and_burrows_positions()
food_eaten = 0


while True:
    move = input()
    snake_next_position = (snake_position[0] + snake_moves[move][0], snake_position[1] + snake_moves[move][1])

    if valid_next_position():

        if matrix[snake_next_position[0]][snake_next_position[1]] == "*":
            food_eaten += 1
            matrix_arrange()
            if food_eaten == 10:
                print("You won! You fed the snake.")
                break

        elif matrix[snake_next_position[0]][snake_next_position[1]] == "B":
            matrix[snake_next_position[0]][snake_next_position[1]] = "."
            burrows_positions.remove(snake_next_position)
            snake_next_position = burrows_positions[0]
            matrix_arrange()

        else:
            matrix_arrange()

    else:
        print("Game over!")
        matrix[snake_position[0]][snake_position[1]] = "."
        break

    snake_position = snake_next_position

print(f"Food eaten: {food_eaten}")

[print(''.join(x)) for x in matrix]