from collections import deque


def check_type_of_bomb(e, p):
    sum_elements = e + p

    if sum_elements % 5 == 0 and sum_elements % 3 == 0:
        fireworks_box["Crossette Fireworks:"] += 1

    elif sum_elements % 3 == 0:
        fireworks_box["Palm Fireworks:"] += 1

    elif sum_elements % 5 == 0:
        fireworks_box["Willow Fireworks:"] += 1

    else:
        e -= 1
        firework_effects.append(e)
        explosive_power.append(p)


def check_materials_quantity():
    global firework_effects, explosive_power

    if firework_effects and explosive_power:
        return True

    else:
        if firework_effects:
            explosive_power = False
        else:
            firework_effects = False
        return False


def check_value(e, p):
    if e <= 0:
        e = False
    if p <= 0:
        p = False
    return e, p


def check_bombs_quantity():
    for value in fireworks_box.values():
        if value < 3:
            return False
    return True


firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = deque([int(x) for x in input().split(", ")])
fireworks_box = {"Palm Fireworks:": 0, "Willow Fireworks:": 0, "Crossette Fireworks:": 0}

while True:

    if check_materials_quantity():
        effect = firework_effects.popleft()
        power = explosive_power.pop()
        effect, power = check_value(effect, power)
        if effect and power:
            check_type_of_bomb(effect, power)

        else:
            if effect:
                firework_effects.appendleft(effect)
            else:
                explosive_power.append(power)
            continue

    else:
        print("Sorry. You can't make the perfect firework show.")
        break

    if check_bombs_quantity():
        print("Congrats! You made the perfect firework show!")
        break


if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")

if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")


{print(key, value) for key,value in fireworks_box.items()}
