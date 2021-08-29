string = input()
final_string = "" + string[0]
for index in range(1,len(string)):
    if string[index] != string[index - 1]:
        final_string += string[index]
print(final_string)