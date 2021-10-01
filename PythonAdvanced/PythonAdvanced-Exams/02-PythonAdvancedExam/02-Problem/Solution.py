from math import floor
def check_player_initial_position():
    for row in range(size_of_matrix):
        for col in range(size_of_matrix):
            if matrix[row][col] == "P":
                return row, col


def check_next_position():
    global collected_coins
    row = next_move[0]
    col = next_move[1]

    if 0 <= row < size_of_matrix and 0 <= col < size_of_matrix:
        if matrix[row][col] != "X":
            collected_coins += matrix[row][col]
            positions_of_collected_coins.append([row, col])
            return True

    collected_coins = floor(collected_coins - (collected_coins * 0.5))

    return False


moves_mapper = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1)
}


size_of_matrix = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size_of_matrix)]
player_position = check_player_initial_position()
collected_coins = 0
positions_of_collected_coins = []


while True:
    move = input()

    if move in moves_mapper:
        next_move = player_position[0] + moves_mapper[move][0], player_position[1] + moves_mapper[move][1]

        if check_next_position():
            player_position = next_move

        else:
            print(f"Game over! You've collected {collected_coins} coins.")
            break

    if collected_coins >= 100:
        print(f"You won! You've collected {collected_coins} coins.")
        break


print("Your path: ")
[print(x) for x in positions_of_collected_coins]
