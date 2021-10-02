from collections import deque


def check_quantity(mens, womens):
    if not mens:
        mens = "none"

    if not womens:
        womens = "none"

    return mens, womens


def check_value(m, w):
    if m <= 0:
        m = False

    elif m % 25 == 0:

        if males:
            males.pop()
        m = False

    if w <= 0:
        w = False

    elif w % 25 == 0 and w != 0:

        if females:
            females.popleft()
        w = False

    return m, w


males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
matches = 0

while True:
    if males and females:

        men = males.pop()
        woman = females.popleft()

        men, woman = check_value(men, woman)

        if men and woman:
            if men == woman:
                matches += 1

            else:
                men -= 2
                males.append(men)

        else:
            if men:
                males.append(men)

            else:
                females.appendleft(woman)

    else:
        males, females = check_quantity(males, females)
        break

print(f"Matches: {matches}")
print(f"Males left: {', '.join([str(x) for x in reversed(males)]) if males != 'none' else males}")
print(f"Females left: {', '.join([str(x) for x in females]) if females != 'none' else females}")
