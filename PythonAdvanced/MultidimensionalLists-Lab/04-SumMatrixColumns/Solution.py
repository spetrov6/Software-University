row,column = [int(x) for x in input().split(", ")]
matrix = []
result = 0
for _ in range(row):
    matrix.append([int(x) for x in input().split()])
for c in range(column):
    for r in range(row):
        result += matrix[r][c]
    print(result)
    result = 0
