from collections import deque


def clock(h, m, s):
    if s < 59:
        s += 1
    else:
        s = 0
        if m < 59:
            m += 1
        else:
            m = 0
            if h < 23:
                h += 1
            else:
                h = 0
    return h, m, s


robots = {}
for robot in input().split(";"):
    key, value = robot.split("-")
    robots[key] = int(value)
hours, minutes, seconds = [int(x) for x in input().split(":")]
products = deque()
working_robots = deque()
free_robots = deque([list(x) for x in robots.items()])
robots_to_free = deque()
product = input()
while product != "End":
    products.append(product)
    product = input()
while products:
    hours, minutes, seconds = clock(hours, minutes, seconds)
    if len(free_robots) == 0:
        products.rotate(-1)
    else:
        print(f"{free_robots[0][0]} - {products.popleft()} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
        working_robots.append(free_robots.popleft())
    if len(working_robots) > 0:
        for robot in working_robots:
            robot[1] = int(robot[1]) - 1
            if int(robot[1]) <= 0:
                free_robots.append([robot[0], robots.get(robot[0])])
                robots_to_free.append(robot)
        if len(robots_to_free) > 0:
            while robots_to_free:
                working_robots.remove(robots_to_free.pop())

