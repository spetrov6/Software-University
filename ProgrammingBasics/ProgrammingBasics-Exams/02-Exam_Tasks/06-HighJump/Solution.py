desired_hight = int(input())
hight_successfull = 0
bar = desired_hight - 30
count_jumps = 0
count_fails = 0
while hight_successfull < desired_hight:
    for i in range(3):
        jump = int(input())
        if jump > desired_hight and bar >= desired_hight:
            hight_successfull = jump
            count_jumps += 1
            break
        elif jump > bar:
            bar += 5
            count_jumps += 1
            break
        else:
            count_fails += 1
            count_jumps += 1
    if count_fails == 3:
        break
    else:
        count_fails = 0
if count_fails == 3:
    print(f"Tihomir failed at {bar}cm after {count_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {bar}cm after {count_jumps} jumps.")
