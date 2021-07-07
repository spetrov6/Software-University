first_line = [int(i) for i in input().split()]
second_line = [int(i) for i in input().split()]
third_line = [int(i) for i in input().split()]
tik_tak_list = [first_line] + [second_line] + [third_line]
if tik_tak_list[0][0] == tik_tak_list[0][1] and tik_tak_list[0][0] == tik_tak_list[0][2] and tik_tak_list[0][0] != 0:
    if tik_tak_list[0][0] == 1:
        print("First player won")
    elif tik_tak_list[0][0] == 2:
        print("Second player won")
elif tik_tak_list[1][0] == tik_tak_list[1][1] and tik_tak_list[1][0] == tik_tak_list[1][2] and tik_tak_list[1][0] != 0:
    if tik_tak_list[1][0] == 1:
        print("First player won")
    elif tik_tak_list[1][0] == 2:
        print("Second player won")
elif tik_tak_list[2][0] == tik_tak_list[2][1] and tik_tak_list[2][0] == tik_tak_list[2][2] and tik_tak_list[2][0] != 0 :
    if tik_tak_list[2][0] == 1:
        print("First player won")
    elif tik_tak_list[2][0] == 2:
        print("Second player won")
elif tik_tak_list[0][2] == tik_tak_list[1][2] and tik_tak_list[0][2] == tik_tak_list[2][2] and tik_tak_list[0][2] != 0:
    if tik_tak_list[0][2] == 1:
        print("First player won")
    elif tik_tak_list[0][2] == 2:
        print("Second player won")
elif tik_tak_list[0][1] == tik_tak_list[1][1] and tik_tak_list[0][1] == tik_tak_list[2][1] and tik_tak_list[0][1] != 0:
    if tik_tak_list[0][1] == 1:
        print("First player won")
    elif tik_tak_list[0][1] == 2:
        print("Second player won")
elif tik_tak_list[0][0] == tik_tak_list[1][0] and tik_tak_list[0][0] == tik_tak_list[2][0] and tik_tak_list[0][0] != 0:
    if tik_tak_list[0][0] == 1:
        print("First player won")
    elif tik_tak_list[0][0] == 2:
        print("Second player won")
elif tik_tak_list[0][0] == tik_tak_list[1][1] and tik_tak_list[0][0] == tik_tak_list[2][2] and tik_tak_list[0][0] != 0:
    if tik_tak_list[0][0] == 1:
        print("First player won")
    elif tik_tak_list[0][0] == 2:
        print("Second player won")
elif tik_tak_list[0][2] == tik_tak_list[1][1] and tik_tak_list[0][2] == tik_tak_list[2][0] and tik_tak_list[0][2] != 0:
    if tik_tak_list[0][2] == 1:
        print("First player won")
    elif tik_tak_list[0][2] == 2:
        print("Second player won")
else:
    print("Draw!")

