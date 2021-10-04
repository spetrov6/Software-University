from collections import deque


def check_materials_quantity():
    global bombs_effect, bombs_casing
    if bombs_effect and bombs_casing:
        return True
    return False


def check_pouch():
    for bombs_count in pouch.values():
        if bombs_count < 3:
            return False
    return True


def check_bomb_type():
    if current_bomb in bombs_types.keys():
        pouch[bombs_types[current_bomb]] += 1
        bombs_effect.popleft()
        bombs_casing.pop()
    else:
        bombs_casing[-1] -= 5


bombs_types = {40: "Datura Bombs:", 60: "Cherry Bombs:", 120: "Smoke Decoy Bombs:"}
pouch = {"Cherry Bombs:": 0, "Datura Bombs:": 0, "Smoke Decoy Bombs:": 0}
current_material = 0
bombs_effect = deque([int(x) for x in input().split(", ")])
bombs_casing = deque([int(x) for x in input().split(", ")])


while True:

    if check_materials_quantity():
        current_bomb = bombs_effect[0] + bombs_casing[-1]
        check_bomb_type()
        if check_pouch():
            print("Bene! You have successfully filled the bomb pouch!")
            break
    else:
        print("You don't have enough materials to fill the bomb pouch.")
        break


if not bombs_effect:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(x) for x in bombs_effect])}")


if not bombs_casing:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(x) for x in bombs_casing])}")


{print(key, value) for key, value in pouch.items()}