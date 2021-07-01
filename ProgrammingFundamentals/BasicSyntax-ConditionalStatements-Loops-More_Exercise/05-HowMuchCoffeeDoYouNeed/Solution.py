command = input()
coffe = 0
command_lower = ["coding","dog","cat","movie"]
command_upper = ["CODING","DOG","CAT","MOVIE"]
while command != "END":
    if command in command_lower:
        coffe += 1
    elif command in command_upper:
        coffe += 2
    command = input()
if coffe > 5:
    print("You need extra sleep")
else:
    print(coffe)