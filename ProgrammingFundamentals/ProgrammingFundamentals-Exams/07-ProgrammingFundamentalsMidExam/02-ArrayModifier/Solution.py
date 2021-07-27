array = [int(i) for i in input().split()]
command_string = input()
while command_string != "end":
    command_list = command_string.split()
    command = command_list[0]
    if len(command_list) == 3:
       index1 = int(command_list[1])
       index2 = int(command_list[2])
    if command == "swap":
        array[index1],array[index2] = array[index2],array[index1]
    elif command == "multiply":
        array[index1] = array[index1] * array[index2]
    else:
        for index in range(len(array)):
            array[index] -= 1
    command_string = input()
print(*array,sep=", ")