size_of_board = int(input())
matrix = []
result = 0
for row in range(size_of_board):
    matrix.append([int(x) for x in input().split()])
    result += matrix[row][row]
print(result)