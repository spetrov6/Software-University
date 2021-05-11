book = input()
name = input()
check = 0

while name != "No More Books":
    if name == book:
        print(f"You checked {check} books and found it.")
        break
    check += 1
    name = input()
if name == "No More Books":
    print(f"The book you search is not here!\nYou checked {check} books. ")
