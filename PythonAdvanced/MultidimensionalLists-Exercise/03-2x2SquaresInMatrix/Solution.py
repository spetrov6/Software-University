rows,cols = [int(x) for x in input().split()]
matrix = [[el for el in input().split()]for x in range(rows)]
sub_matrix_count = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1]\
            and matrix[row][col] == matrix[row+1][col] and matrix[row][col] == matrix[row+1][col+1]:
            sub_matrix_count +=1
print(sub_matrix_count)