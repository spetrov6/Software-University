expression = input()
test_list = []
for index in range(len(expression)):
    if expression[index] == "(":
        test_list.append(index)
    elif expression[index] == ")":
        print(expression[test_list[-1]:index + 1])
        test_list.pop()