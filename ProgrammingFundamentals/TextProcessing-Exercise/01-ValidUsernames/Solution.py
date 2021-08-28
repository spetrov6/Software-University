names = input().split(", ")
for name in names:
    name_is_valid = False
    if 3 <= len(name) <= 16:
        for letter in name:
            if not letter.isalpha() and not letter.isdigit() and not letter == "_" and not letter == "-":
                name_is_valid = False
                break
            name_is_valid = True
    if name_is_valid:
        print(name)
