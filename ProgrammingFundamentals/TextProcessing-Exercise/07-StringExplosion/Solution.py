string = list(input())
bomb = 0
for index in range(len(string)):
    if bomb > 0 and string[index] != ">":
        string[index] = 0
        bomb -= 1
    elif string[index] == ">":
        bomb += int(string[index + 1])
while 0 in string:
    string.remove(0)
print("".join(string))
