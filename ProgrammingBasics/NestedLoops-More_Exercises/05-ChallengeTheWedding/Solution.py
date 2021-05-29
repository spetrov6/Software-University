mens = int(input())
womans = int(input())
tables = int(input())
count = 0
full = False
for men in range(1, mens + 1):
    for woman in range(1, womans + 1):
        count += 1
        print(f"({men} <-> {woman})", end=" ")
        if count >= tables:
            full = True
            break
    if full:
        break

