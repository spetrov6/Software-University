n = int(input())
open_pren = 0
closed_pren = 0
last = ""
for i in range(n):
    character = input()
    if character == "(":
        open_pren += 1
    elif character == ")":
        closed_pren += 1
    if last == "(" and character == "(" or last == ")" and character == ")":
        open_pren -= 1
    last = character
if open_pren == closed_pren:
    print("BALANCED")
else:
    print("UNBALANCED")
