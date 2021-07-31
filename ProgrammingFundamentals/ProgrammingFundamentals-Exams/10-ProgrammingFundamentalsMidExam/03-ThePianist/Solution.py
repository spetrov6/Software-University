number_of_pieces = int(input())
pieces = {}
for _ in range(number_of_pieces):
    piece,composer,key = input().split("|")
    pieces[piece] = {"composer":composer,"key":key}
command = input()
while command != "Stop":
    actions = command.split("|")
    if actions[0] == "Add":
        if actions[1] in pieces:
            print(f"{actions[1]} is already in the collection!")
        else:
            pieces[actions[1]] = {"composer":actions[2],"key":actions[3]}
            print(f"{actions[1]} by {actions[2]} in {actions[3]} added to the collection!")
    elif actions[0] == "Remove":
        if actions[1] in pieces:
            pieces.pop(actions[1])
            print(f"Successfully removed {actions[1]}!")
        else:
            print(f"Invalid operation! {actions[1]} does not exist in the collection.")
    elif actions[0] == "ChangeKey":
        if actions[1] in pieces:
            pieces[actions[1]]["key"] = actions[2]
            print(f"Changed the key of {actions[1]} to {actions[2]}!")
        else:
            print(f"Invalid operation! {actions[1]} does not exist in the collection.")
    command = input()
pieces = dict(sorted(pieces.items(),key=lambda kvp: (kvp[0],kvp[1]["composer"])))
for key,value in pieces.items():
    print(f'{key} -> Composer: {value.get("composer")}, Key: {value.get("key")}')

