strings = input().split()
total_sum = 0
if len(strings[0]) >= len(strings[1]):
    first_string = strings[0]
    second_string = strings[1]
else:
    first_string = strings[1]
    second_string = strings[0]
for i in range(len(first_string)):
    if i < len(second_string):
        total_sum += ord(first_string[i]) * ord(second_string[i])
    else:
        total_sum += ord(first_string[i])
print(total_sum)