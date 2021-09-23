from collections import deque

def field_function():
    size_of_field = int(input())
    directions = deque([x for x in input().split()])
    area = [[x for x in input().split()] for _ in range(size_of_field)]
    return area,directions

def check_positions_of_elements(area):
    miner_position = []
    coal_positions = []
    for row in range(len(field)):
        for col in range(len(field)):
            current_cell = field[row][col]
            if current_cell == "s":
                miner_position = [row,col]
            elif current_cell == "c":
                coal_positions.append([row,col])
    return miner_position,coal_positions

def miner_next_position_function(minor_current_position,move_direction):
    row_current,col_current = minor_current_position[0],minor_current_position[1]
    if direction == "up":
        return row_current - 1,col_current
    elif direction == "down":
        return row_current + 1, col_current
    elif direction == "left":
        return row_current, col_current - 1
    elif direction == "right":
        return row_current,col_current + 1

def valid_next_position(next_position,area):
    row,col = miner_next_position[0],miner_next_position[1]
    if not 0 <= row <= len(area) - 1 or not 0 <= col <= len(area) - 1:
        return False
    return True

field, moving_directions = field_function()
miner_position, coal_positions = check_positions_of_elements(field)
founded_coal_count = 0

while moving_directions:
    direction = moving_directions[0]
    miner_next_position = miner_next_position_function(miner_position,direction)
    if valid_next_position(miner_next_position,field):
        row_next,col_next = miner_next_position[0],miner_next_position[1]
        if field[row_next][col_next] == "e":
            print(f"Game over! {row_next,col_next}")
            break
        elif field[row_next][col_next] == "*":
            field[miner_position[0]][miner_position[1]] = "*"
            field[row_next][col_next] = "s"
            miner_position[0],miner_position[1] = row_next,col_next
        elif field[row_next][col_next] == "c":
            founded_coal_count += 1
            field[miner_position[0]][miner_position[1]] = "*"
            field[row_next][col_next] = "s"
            miner_position[0], miner_position[1] = row_next, col_next
            coal_positions.remove([row_next,col_next])
            if not coal_positions:
                print(f"You collected all coals! {row_next,col_next}")
                break
    moving_directions.popleft()
if not moving_directions:
    print(f"{len(coal_positions)} coals left. {row_next,col_next}")