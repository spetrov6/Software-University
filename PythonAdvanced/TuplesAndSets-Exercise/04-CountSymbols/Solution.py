text = sorted(tuple(input()))
for character in sorted(set(text),key=text.index):
    print(f"{character}: {text.count(character)} time/s")