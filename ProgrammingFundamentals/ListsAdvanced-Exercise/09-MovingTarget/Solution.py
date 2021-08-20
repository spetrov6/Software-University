targets_health = [int(i) for i in input().split()]
command = input()
while command != "End":
    task,index,value = command.split()
    if task == "Shoot":
        if 0 <= int(index) < len(targets_health):
            targets_health[int(index)] -= int(value)
            if targets_health[int(index)] <= 0:
                targets_health.pop(int(index))
    elif task == "Add":
        if 0 <= int(index) < len(targets_health):
            targets_health.insert(int(index),int(value))
        else:
            print("Invalid placement!")
    else:
        if int(index) - int(value) >= 0 and int(index) + int(value) < len(targets_health):
            for i in targets_health[int(index) - int(value):int(index) + int(value) + 1]:
                targets_health.remove(i)
        else:
            print("Strike missed!")
    command = input()
print(*targets_health,sep="|")