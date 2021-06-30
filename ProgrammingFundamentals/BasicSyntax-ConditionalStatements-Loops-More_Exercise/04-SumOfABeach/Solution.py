word = list(input().lower())
count = 0
for index in range(len(word)):
    if word[index] == "f" and index + 3 <= len(word):
        if word[index + 1] == "i" and word[index + 2] == "s" and word[index + 3] == "h":
            count += 1
    if word[index] == "s" and index + 3 <= len(word):
        if word[index + 1] == "a" and word[index + 2] == "n" and word[index + 3] == "d":
            count += 1
    if word[index] == "s" and index + 2 <= len(word):
        if word[index + 1] == "u" and word[index + 2] == "n":
            count += 1
    if word[index] == "w" and index + 4 <= len(word):
        if word[index + 1] == "a" and word[index + 2] == "t" and word[index + 3] == "e" and word[index + 4] == "r":
            count += 1
print(count)
