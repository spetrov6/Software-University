size_of_board = int(input())
matrix = [[x for x in input()]for x in range(size_of_board)]
symbol_found = False
symbol = input()
for row in range(size_of_board):
    for col in range(size_of_board):
        if matrix[row][col] == symbol:
            print((row,col))
            symbol_found = True
            exit()
if not symbol_found:
    print(f"{symbol} does not occur in the matrix")