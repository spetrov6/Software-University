from collections import deque
cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])
wasted_water = 0
while True:
    if cups[0] <= bottles[-1]:
        wasted_water += bottles[-1] - cups[0]
        cups.popleft()
        bottles.pop()
    elif cups[0] > bottles[-1]:
        cups[0] = cups[0] - bottles[-1]
        bottles.pop()
    if len(cups) == 0:
        bottles.reverse()
        print(f"Bottles: {' '.join([str(x) for x in bottles])}")
        break
    elif len(bottles) == 0:
        print(f"Cups: {' '.join([str(x) for x in cups])}")
        break
print(f"Wasted litters of water: {wasted_water}")