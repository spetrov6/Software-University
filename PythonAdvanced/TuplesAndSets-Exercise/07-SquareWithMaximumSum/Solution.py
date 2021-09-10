rows,cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")]for x in range(rows)]
top_left_sum = 0
top_left_position = (0, 0)
for row in range(rows -1):
    for col in range(cols -1):
        if matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1] > top_left_sum:
            top_left_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
            top_left_position = (row, col)
row,col = top_left_position
print(f"{matrix[row][col]} {matrix[row][col+1]}\n{matrix[row+1][col]} {matrix[row+1][col+1]}")
print(top_left_sum)