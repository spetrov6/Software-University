row,col = [int(x) for x in input().split()]
matrix = [[el for el in input().split()] for x in range(row)]
command = input()
while command != "END":
    try:
        swap,row1,col1,row2,col2 = command.split()[0],int(command.split()[1]),\
                               int(command.split()[2]),int(command.split()[3]),int(command.split()[4])
        if swap == "swap":
            matrix[row1][col1],matrix[row2][col2] = matrix[row2][col2],matrix[row1][col1]
            [print(' '.join(x)) for x in matrix]
        else:
            print("Invalid input!")
    except:
        print("Invalid input!")
    command = input()
