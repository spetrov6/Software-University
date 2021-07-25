energy = int(input())
command = input()
victory = 0
win = True
while command != "End of battle":
    command = int(command)
    if energy >= command:
        energy -= command
        victory += 1
        if victory % 3 == 0:
            energy += victory
    else:
        print(f"Not enough energy! Game ends with {victory} won battles and {energy} energy")
        win = False
        break
    command = input()
if win:
    print(f"Won battles: {victory}. Energy left: {energy}")