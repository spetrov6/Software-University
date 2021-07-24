number_of_heroes = int(input())
heroes_info = {}
for _ in range(number_of_heroes):
    hero,hit,mana = input().split()
    heroes_info[hero] = {"hit":int(hit),"mana":int(mana)}
command = input()
while command != "End":
    actions = command.split(" - ")
    if actions[0] == "CastSpell":
        name,MP_needed,spell_name = actions[1],int(actions[2]),actions[3]
        if heroes_info[name]["mana"] >= MP_needed:
            heroes_info[name]["mana"] -= MP_needed
            print(f'{name} has successfully cast {spell_name} and now has {heroes_info[name]["mana"]} MP!')
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif actions[0] == "TakeDamage":
        name,damage,attacker = actions[1],int(actions[2]),actions[3]
        heroes_info[name]["hit"] -= damage
        if heroes_info[name]["hit"] > 0:
            print(f'{name} was hit for {damage} HP by {attacker} and now has {heroes_info[name]["hit"]} HP left!')
        else:
            heroes_info.pop(name)
            print(f"{name} has been killed by {attacker}!")
    elif actions[0] == "Recharge":
        name,amount = actions[1],int(actions[2])
        if heroes_info[name]["mana"] + amount <= 200:
            heroes_info[name]["mana"] += amount
            print(f'{name} recharged for {amount} MP!')
        else:
            print(f'{name} recharged for {200 - heroes_info[name]["mana"]} MP!')
            heroes_info[name]["mana"] += 200 - heroes_info[name]["mana"]
    elif actions[0] == "Heal":
        name, amount = actions[1], int(actions[2])
        if heroes_info[name]["hit"] + amount <= 100:
            heroes_info[name]["hit"] += amount
            print(f'{name} healed for {amount} HP!')
        else:
            print(f'{name} healed for {100 - heroes_info[name]["hit"]} HP!')
            heroes_info[name]["hit"] += 100 - heroes_info[name]["hit"]
    command = input()
heroes_info = dict(sorted(heroes_info.items(),key=lambda kvp:(-kvp[1]["hit"],kvp[0])))
for key,value in heroes_info.items():
    print(f'{key}')
    print(f'  HP: {value["hit"]}')
    print(f'  MP: {value["mana"]}')