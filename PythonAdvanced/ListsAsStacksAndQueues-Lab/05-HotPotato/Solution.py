from _collections import deque
kids_names = deque(input().split())
toss_count = int(input())
test = []
while len(kids_names) > 1:
    test.append(kids_names.popleft())
    if len(test) == toss_count:
        print(f"Removed {test.pop()}")
        test = []
    else:
        kids_names.append(test[-1])
print(f"Last is {kids_names.popleft()}")