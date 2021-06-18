name = input()
games = int(input())
points = 0
w = 0
d = 0
l = 0
for i in range(games):
    result = input()
    if result == "W":
        points += 3
        w += 1
    elif result == "D":
        points += 1
        d += 1
    else:
        l += 1
if games <= 0:
    print(f"{name} hasn't played any games during this season.")
else:
    print(f"{name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {w}")
    print(f"## D: {d}")
    print(f"## L: {l}")
    print(f"Win rate: {w / games * 100:.2f}%")