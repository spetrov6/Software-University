from math import floor
def longest_line(first_line, second_line):
    first_line_length = ((first_line[2] - first_line[0]) ** 2 + (first_line[3] - first_line[1]) ** 2)
    second_line_length = ((second_line[2] - second_line[0]) ** 2 + (second_line[3] - second_line[1]) ** 2)
    if first_line_length >= second_line_length:
        first_line = [floor(i) for i in first_line]
        closer_point([first_line[0], first_line[1]], [first_line[2], first_line[3]])
    else:
        second_line = [floor(i) for i in second_line]
        closer_point([second_line[0], second_line[1]], [second_line[2], second_line[3]])
def closer_point(x,y):
    if abs(sum(x)) <= abs(sum(y)):
        print(f"({x[0]}, {x[1]})({y[0]}, {y[1]})")
    elif abs(sum(y)) < abs(sum(x)):
        print(f"({y[0]}, {y[1]})({x[0]}, {x[1]})")
first_line_input = [float(input()) for _ in range(4)]
second_line_input = [float(input()) for _ in range(4)]
longest_line(first_line_input,second_line_input)