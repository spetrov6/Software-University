sequence = [int(i) for i in input().split()]
command = input()
shoot = 0
last_target_value = 0
while command != "End":
    command = int(command)
    if 0 <= command < len(sequence):
        if sequence[command] > -1:
            last_target_value = sequence[command]
            sequence[command] = -1
            for index in range(len(sequence)):
                if sequence[index] > -1:
                    if sequence[index] > last_target_value:
                        sequence[index] -= last_target_value
                    else:
                        sequence[index] += last_target_value
                else:
                    continue
            shoot += 1
    command = input()
print(f"Shot targets: {shoot} -> ",end="")
print(*sequence,sep=" ")