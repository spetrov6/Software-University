sentence = input().lower().split()
words = {}
words_as_list = []
for i in sentence:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1
for key,value in words.items():
    if words[key] % 2 != 0:
        words_as_list.append(key)
print(" ".join(words_as_list))

