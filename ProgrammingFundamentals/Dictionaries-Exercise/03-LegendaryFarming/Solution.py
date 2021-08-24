legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_materials = {"fragments": 0, "motes": 0,"shards": 0}
legendary_item_obtained = False
junks = {}
while not legendary_item_obtained:
    materials_as_list = input().split()
    for x in range(0,len(materials_as_list),2):
        material = materials_as_list[x + 1].lower()
        quantity = int(materials_as_list[x])
        if material in key_materials and key_materials[material] + quantity < 250:
            key_materials[material] += quantity
        elif material in key_materials and key_materials[material] + quantity >= 250:
            legendary_item_obtained = True
            key_materials[material] += quantity - 250
            print(f"{legendary_items[material]} obtained!")
            break
        else:
            if material in junks:
                junks[material] += quantity
            else:
                junks[material] = quantity
key_materials = sorted(key_materials.items(),key=lambda kvp: (-kvp[1],kvp[0]))
junks = sorted(junks.items())
for key,value in key_materials:
    print(f"{key}: {value}")
for key,value in junks:
    print(f"{key}: {value}")

