n = int(input())
list_num = []
final_list = []
for _ in range(n):
    num = int(input())
    list_num.append(num)
command = input()
for j in list_num:
    if command == "even":
        if j % 2 == 0 or j == 0:
            final_list.append(j)
    elif command == "odd":
        if j % 2 != 0:
            final_list.append(j)
    elif command == "negative":
        if j < 0:
            final_list.append(j)
    elif command == "positive":
        if j >= 0:
            final_list.append(j)
print(final_list)