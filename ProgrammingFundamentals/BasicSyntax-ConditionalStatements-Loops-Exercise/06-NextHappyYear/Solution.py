num = int(input()) + 1
while True:
    word = str(num)
    if len(set(word)) != len(word):
        num += 1
    else:
        print(num)
        break