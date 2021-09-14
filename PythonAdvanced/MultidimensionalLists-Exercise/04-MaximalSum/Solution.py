rows,cols = [int(x) for x in input().split()]
matrix = [[int(el) for el in input().split()]for row in range(rows)]
sub_matrix_max_sum = -1
max_sub_matrix = []
for row in range(rows - 2):
    for col in range(cols - 2):
        sub_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
                      matrix[row + 1][col], matrix[row + 1][col + 1],
                      matrix[row + 1][col + 2],matrix[row + 2][col],
                      matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        if sum(sub_matrix) > sub_matrix_max_sum:
            max_sub_matrix = sub_matrix
            sub_matrix_max_sum = sum(sub_matrix)
print(f"Sum = {sub_matrix_max_sum}")
max_sub_matrix = [[str(max_sub_matrix.pop(0)) for el in range(3)] for x in range(3)]
[print(' '.join(x)) for x in max_sub_matrix]
