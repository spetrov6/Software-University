def sum_points():
    positions_mapper = [[0, col], [6, col], [row, 0], [row, 6]]
    points = 0
    for position in positions_mapper:
        points += int(dart[position[0]][position[1]])
    return points


players = {x: {"points": 501, "throws": 0} for x in input().split(", ")}
dart = [[x for x in input().split()] for _ in range(7)]
win = False

while True:
    for player in players:
        throw_position = list(filter(lambda x: x.isdigit(), input()))
        row, col = int(throw_position[0]), int(throw_position[1])

        if 0 <= row < 7 and 0 <= col < 7:
            if dart[row][col].isdigit():
                players[player]["points"] -= int(dart[row][col])
                players[player]["throws"] += 1

            elif dart[row][col] == "D":
                players[player]["points"] -= sum_points() * 2
                players[player]["throws"] += 1

            elif dart[row][col] == "T":
                players[player]["points"] -= sum_points() * 3
                players[player]["throws"] += 1

            else:
                players[player]["throws"] += 1
                print(f"{player} won the game with {players[player]['throws']} throws!")
                win = True
                break

        else:
            players[player]["throws"] += 1

        if players[player]["points"] <= 0:
            print(f"{player} won the game with {players[player]['throws']} throws!")
            win = True
            break
    if win:
        break
