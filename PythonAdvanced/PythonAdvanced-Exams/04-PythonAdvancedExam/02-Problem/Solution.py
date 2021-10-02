from collections import deque


def check_player_initial_position():
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "P":
                return row, col


def next_position():
    row = player_position[0] + moves_mapper[move][0]
    col = player_position[1] + moves_mapper[move][1]
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return row,col
    return False


moves_mapper = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1)
}


initial_string = input()
matrix_size = int(input())
matrix = [[x for x in input()] for _ in range(matrix_size)]
moves_count = int(input())
moves = deque([input() for _ in range(moves_count)])
player_position = check_player_initial_position()


while moves:
    move = moves.popleft()
    next_player_position = next_position()

    if next_player_position:
        if matrix[next_player_position[0]][next_player_position[1]] != "-":
            initial_string += matrix[next_player_position[0]][next_player_position[1]]

        matrix[player_position[0]][player_position[1]] = "-"
        matrix[next_player_position[0]][next_player_position[1]] = "P"

    else:
        player_position = player_position
        if initial_string:
            initial_string = initial_string[:-1]
        continue

    player_position = next_player_position

print(initial_string)
[print(''.join(x)) for x in matrix]