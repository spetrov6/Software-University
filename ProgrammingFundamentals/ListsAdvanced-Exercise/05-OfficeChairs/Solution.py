n = int(input())
free_chairs = 0
count = 0
enough_chairs = True
for i in range(n):
    room = [i for i in input().split()]
    chairs_taken = int(room[1])
    chairs_in_room = len(room[0])
    count += 1
    if chairs_in_room == chairs_taken:
        continue
    elif chairs_in_room < chairs_taken:
        print(f"{chairs_taken - chairs_in_room} more chairs needed in room {count}")
        enough_chairs = False
    else:
        free_chairs += chairs_in_room - chairs_taken
if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")