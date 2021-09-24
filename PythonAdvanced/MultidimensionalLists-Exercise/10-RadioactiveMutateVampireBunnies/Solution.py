from collections import deque

def field_function():
    size_of_field = [int(x) for x in input().split()]
    area = [[x for x in input()] for _ in range(size_of_field[0])]
    directions = deque([x for x in input()])
    return area,directions

def check_player_position(area):
    player_position = []
    for row in range(len(area)):
        for col in range(len(area[row])):
            current_cell = area[row][col]
            if current_cell == "P":
                player_position = [row,col]
    return player_position

def check_bunnies_positions(area):
    bunny_positions = []
    for row in range(len(area)):
        for col in range(len(area[row])):
            current_cell = area[row][col]
            if current_cell == "B":
                bunny_positions.append([row,col])
    return bunny_positions

def player_next_position_function(player_current_position, move_direction):
    row_current,col_current = player_current_position[0],player_current_position[1]
    if direction == "U":
        return row_current - 1,col_current
    elif direction == "D":
        return row_current + 1, col_current
    elif direction == "L":
        return row_current, col_current - 1
    elif direction == "R":
        return row_current,col_current + 1

def is_next_position_exit(player_next_position, area):
    row,col = player_next_position[0],player_next_position[1]
    if not 0 <= row <= len(area) - 1 or not 0 <= col <= len(area[0]) - 1:
        return True
    return False

def valid_position_for_bunny(next_position,area):
    global player_found
    row_bunny,col_bunny = next_position[0],next_position[1]
    if not 0 <= row_bunny <= len(area) - 1 or not 0 <= col_bunny <= len(area[0]) - 1:
        return False
    if area[row_bunny][col_bunny] == "B":
        return False
    if area[row_bunny][col_bunny] == "P":
        player_found = True
    return True
def bunnies_spread(bunnies,area):
    for bunny in bunnies:
        bunny_current_row,bunny_current_col = bunny[0],bunny[1]
        if valid_position_for_bunny([bunny_current_row - 1,bunny_current_col],area):      #UP
            area[bunny_current_row - 1][bunny_current_col] = "B"
        if valid_position_for_bunny([bunny_current_row + 1,bunny_current_col],area):      #DOWN
            area[bunny_current_row + 1][bunny_current_col] = "B"
        if valid_position_for_bunny([bunny_current_row,bunny_current_col - 1],area):      #LEFT
            area[bunny_current_row][bunny_current_col - 1] = "B"
        if valid_position_for_bunny([bunny_current_row,bunny_current_col + 1],area):      #RIGHT
            area[bunny_current_row][bunny_current_col + 1] = "B"
lair, moving_directions = field_function()
player_position = check_player_position(lair)
player_found = False
while True:
    direction = moving_directions[0]
    player_next_position = player_next_position_function(player_position, direction)
    bunnies_positions = check_bunnies_positions(lair)
    if not is_next_position_exit(player_next_position, lair):
        row_next,col_next = player_next_position[0],player_next_position[1]
        if lair[row_next][col_next] == "B":
            bunnies_spread(bunnies_positions, lair)
            [print(''.join(row)) for row in lair]
            print(f"dead: {row_next} {col_next}")
            break
        else:
            lair[player_position[0]][player_position[1]] = "."
            lair[row_next][col_next] = "P"
            player_position[0],player_position[1] = row_next,col_next
        bunnies_spread(bunnies_positions,lair)
        if player_found:
            bunnies_spread(bunnies_positions, lair)
            [print(''.join(row)) for row in lair]
            print(f"dead: {row_next} {col_next}")
            break

    else:
        lair[player_position[0]][player_position[1]] = "."
        bunnies_spread(bunnies_positions, lair)
        [print(''.join(row))for row in lair]
        print(f"won: {player_position[0]} {player_position[1]}")
        break
    moving_directions.popleft()