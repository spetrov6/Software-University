from collections import deque
name = input()
queue_peoples = deque()
while name != "End":
    if name == "Paid":
        while len(queue_peoples) > 0:
            print(queue_peoples.popleft())
    else:
        queue_peoples.append(name)
    name = input()
print(f"{len(queue_peoples)} people remaining.")