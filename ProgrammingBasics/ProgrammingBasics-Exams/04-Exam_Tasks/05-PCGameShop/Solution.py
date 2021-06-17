games = int(input())
hearthstone = 0
fortnite = 0
overwatch = 0
other = 0
for i in range(games):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fortnite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        other += 1
print(f"Hearthstone - {hearthstone / games * 100:.2f}%")
print(f"Fornite - {fortnite / games * 100:.2f}%")
print(f"Overwatch - {overwatch / games * 100:.2f}%")
print(f"Others - {other / games * 100:.2f}%")
