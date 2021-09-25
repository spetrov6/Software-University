def chairs_rotation(names,chairs,players_sit=[]):
    if len(players_sit) == chairs:
        print(', '.join(players_sit))
        count = 0
        return
    for name in range(len(names)):
        players_sit.append(names[name])
        chairs_rotation(names[name+1:],chairs,players_sit)
        players_sit.pop()

names_list = [x for x in input().split(", ")]
chairs_count = int(input())
chairs_rotation(names_list,chairs_count)