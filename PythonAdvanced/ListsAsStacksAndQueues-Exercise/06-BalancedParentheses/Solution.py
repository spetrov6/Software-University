from collections import deque
mapper = {"{":"}","(":")","[":"]"}
parentheses = deque([x for x in input()])
opening = deque()
closing = deque()
balanced = True
while parentheses:
    bracket = parentheses.popleft()
    if bracket in mapper:
        opening.append(bracket)
    else:
        closing.append(bracket)
        try:
            if mapper[opening[-1]] == bracket:
                opening.pop()
                closing.popleft()
            else:
                balanced = False
        except:
            balanced = False
if balanced and len(opening) == len(closing):
    print("YES")
else:
    print("NO")