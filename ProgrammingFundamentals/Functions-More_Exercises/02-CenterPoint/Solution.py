from math import floor
def coordinate(x,y):
    first = abs(x[0]) + abs(x[1])
    second = abs(y[0]) + abs(y[1])
    if first > second:
        y = [floor(i) for i in y]
        print(tuple(y))
    elif second >= first:
        x = [floor(i) for i in x]
        print(tuple(x))
x_y1 = [float(input()) for i in range(2)]
x_y2 = [float(input()) for j in range(2)]
coordinate(x_y1,x_y2)