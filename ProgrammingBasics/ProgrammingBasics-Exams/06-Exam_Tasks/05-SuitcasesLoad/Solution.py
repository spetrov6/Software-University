space = float(input())
command = input()
count = 0
suitcases = 0
space_left = space
while command != "End":
    size = float(command)
    count += 1
    if count == 3:
        size += size * 0.10
        count = 0
        space_left -= size
    else:
        space_left -= size
    if space_left <= 0:
        break
    suitcases += 1
    command = input()
if command == "End":
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {suitcases} suitcases loaded.")
