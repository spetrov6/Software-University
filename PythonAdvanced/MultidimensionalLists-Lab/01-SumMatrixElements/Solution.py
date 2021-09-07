row = input().split(", ")
matrix = []
result = 0
for i in range(int(row[0])):
    matrix.append([int(x) for x in input().split(", ")])
    result += sum(matrix[i])
print(f"{result}\n{matrix}")