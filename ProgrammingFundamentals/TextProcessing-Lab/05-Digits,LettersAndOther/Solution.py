string = input()
digits = ""
letters = ""
chars = ""
for i in string:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        chars += i
print(f"{digits}\n{letters}\n{chars}")