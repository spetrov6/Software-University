size_of_grid = int(input())
matrix = [[int(col) for col in input().split()]for row in range(size_of_grid)]
primary_diagonal_sum = 0
secondary_diagonal_sum = 0
for row in range(size_of_grid):
    primary_diagonal_sum += matrix[row][row]
    secondary_diagonal_sum += matrix[size_of_grid - 1 - row][row]
print(abs(primary_diagonal_sum - secondary_diagonal_sum))