word = input()
word_list = list(word)
count = 0
result = []
for i in word_list:
    if 65 <= ord(i) <= 90:
        result.append(count)
    count += 1
print(result)