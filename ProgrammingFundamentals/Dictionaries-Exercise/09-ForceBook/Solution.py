force_book = input()
force_sides = {}
users = []
while force_book != "Lumpawaroo":
    if "|" in force_book:
        side,user = force_book.split(" | ")
        if user not in users:
            if side not in force_sides:
                force_sides[side] = []
            force_sides[side].append(user)
            users.append(user)
    else:
        user,side = force_book.split(" -> ")
        if user in users:
            for key,value in force_sides.items():
                if user in value:
                    force_sides[key].remove(user)
                    break
        if side not in force_sides:
            force_sides[side] = []
        force_sides[side].append(user)
        users.append(user)
        print(f"{user} joins the {side} side!")
    force_book = input()
force_sides = sorted(force_sides.items(),key=lambda kvp:(-len(kvp[1]),kvp[0]))
for i in force_sides:
    if len(i[1]) > 0:
        print(f"Side: {i[0]}, Members: {len(i[1])}")
        for j in sorted(i[1]):
            print(f"! {j}")
