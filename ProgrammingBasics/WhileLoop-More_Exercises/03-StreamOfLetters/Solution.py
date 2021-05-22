letter = input()
c = 0
o = 0
n = 0
word = ""
while letter != "End":
    if ord(letter) < 65 or 90 < ord(letter) < 97 or ord(letter) > 122 :
        letter = input()
        continue
    if letter == "c":
        if c < 1:
            c += 1
        else:
            word += letter
    elif letter == "o":
        if o < 1:
            o += 1
        else:
            word += letter
    elif letter == "n":
        if n < 1:
            n += 1
        else:
            word += letter
    else:
        word += letter
    if(o + c + n) >= 3:
        print(f"{word}", end=" ")
        word = ""
        o = 0
        n = 0
        c = 0
    letter = input()