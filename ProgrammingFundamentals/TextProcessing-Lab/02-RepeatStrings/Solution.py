final_string = ""
string = input().split()
for i in string:
    final_string += i * len(i)
print(final_string)