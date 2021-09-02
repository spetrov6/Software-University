from collections import deque
quires_count = int(input())
numbers_que = deque()
result = deque()
for _ in range(quires_count):
    quire = input()
    if quire.startswith("1"):
        numbers_que.append(int(quire.split()[1]))
    elif quire == "2":
        try:
            numbers_que.pop()
        except:
            pass
    elif quire == "3":
        try:
            print(max(numbers_que))
        except:
            pass
    else:
        try:
            print(min(numbers_que))
        except:
            pass
while numbers_que:
    result.append(numbers_que.pop())
print(*result,sep=", ")