from collections import deque
clothes = deque([int(x) for x in input().split()])
rack_size = int(input())
rack = 0
rack_counter = 0
while clothes:
    box = clothes.pop()
    if rack == 0:
        rack += box
        rack_counter += 1
    elif box + rack < rack_size:
        rack += box
    elif box + rack > rack_size:
        rack = 0
        clothes.append(box)
    else:
        rack = 0
print(rack_counter)