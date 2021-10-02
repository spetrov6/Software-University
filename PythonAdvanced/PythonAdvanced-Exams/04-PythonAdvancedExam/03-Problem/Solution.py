def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    for row in range(2, n):
        triangle.append([])
        for col in range(row + 1):
            if col == 0:
                triangle[row].append(triangle[row-1][0])
            elif col == len(triangle[row - 1]):
                triangle[row].append(triangle[row-1][-1])
            else:
                num = triangle[row - 1][col - 1] + triangle[row-1][col]
                triangle[row].append(num)
    return triangle