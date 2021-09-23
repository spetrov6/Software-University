from collections import deque

def board_function():
    size_of_board = int(input())
    board = [[int(x) for x in input().split()] for _ in range(size_of_board)]
    return board

def main(board,bombs):
    while bombs:
        row, col = bombs.popleft()
        bomb_blow(board,row,col)
def bomb_blow(board,row_bomb,col_bomb):
    bomb_power = board[row_bomb][col_bomb]
    cels_to_blow = [
                    [row_bomb - 1,col_bomb - 1],[row_bomb - 1,col_bomb],[row_bomb -1 ,col_bomb + 1],
                    [row_bomb,col_bomb - 1],[row_bomb,col_bomb + 1],
                    [row_bomb + 1,col_bomb - 1],[row_bomb + 1,col_bomb],[row_bomb + 1,col_bomb + 1]
                    ]
    if bomb_power > 0:
        for cel in cels_to_blow:
            cel_row,cel_col = cel[0],cel[1]
            if not 0 <= cel_row <= len(board) - 1:
                continue
            if not 0 <= cel_col <= len(board) - 1:
                continue
            if 0 < board[cel_row][cel_col]:
                board[cel_row][cel_col] -= bomb_power
        board[row_bomb][col_bomb] = 0
def check_for_live_cels(board):
    live_cels = 0
    sum_live_cels = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] > 0:
                live_cels += 1
                sum_live_cels += board[row][col]
    print(f"Alive cells: {live_cels}\nSum: {sum_live_cels}")

matrix = board_function()
bombs_coordinates = deque([[int(x) for x in bomb.split(",")] for bomb in input().split()])
main(matrix,bombs_coordinates)
check_for_live_cels(matrix)
matrix = [[str(el) for el in row] for row in matrix]
[print(' '.join(x)) for x in matrix]