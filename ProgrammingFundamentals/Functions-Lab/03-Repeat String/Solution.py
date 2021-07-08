def repeat_string(text,count_of_repeat):
    result = ""
    for _ in range(count_of_repeat):
        result += text
    return result

string = input()
count_for_repeat = int(input())
print(repeat_string(string,count_for_repeat))