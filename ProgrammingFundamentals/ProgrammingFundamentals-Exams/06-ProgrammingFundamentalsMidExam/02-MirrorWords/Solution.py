import re
text = input()
pattern = r"(@|#)[a-zA-Z]{3,}\1\1[a-zA-Z]{3,}\1"
words = [obj.group() for obj in re.finditer(pattern,text)]
mirror_words = []
if len(words) == 0:
    print("No word pairs found!")
if len(words) > 0:
    print(f"{len(words)} word pairs found!")
    for i in words:
        result = []
        if "#" in i:
            result = i.split("#")
        elif "@" in i:
            result = i.split("@")
        while "" in result:
            result.remove("")
        if result[0][::-1] == result[1] or result[0] == result[1][::-1]:
            mirror_words.append(f"{result[0]} <=> {result[1]}")
if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(mirror_words))