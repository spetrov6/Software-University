sequence = input().split()
command = input()
moves = 0
while command != "end":
    command = [int(i) for i in command.split()]
    index1 = command[0]
    index2 = command[1]
    moves += 1
    if index1 == index2 or index1 < 0 or index1 >= len(sequence) or index2 < 0 or index2 >= len(sequence):
        print("Invalid input! Adding additional elements to the board")
        sequence.insert(len(sequence) // 2,"-" + str(moves) + "a")
        sequence.insert(len(sequence) // 2,"-" + str(moves) + "a")
    elif sequence[index1] != sequence[index2]:
        print("Try again!")
    elif sequence[index1] == sequence[index2]:
        print(f"Congrats! You have found matching elements - {sequence[index1]}!")
        element_to_remove = sequence[index1]
        for i in range(len(sequence)):
            if element_to_remove in sequence:
                sequence.remove(element_to_remove)
    if len(sequence) == 0:
        break
    command = input()
if len(sequence) == 0:
    print(f"You have won in {moves} turns!")
else:
    print("Sorry you lose :(")
    print(*sequence,sep=" ")
