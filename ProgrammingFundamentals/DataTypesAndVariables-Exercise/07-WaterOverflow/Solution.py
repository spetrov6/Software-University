n = int(input())
capacity = 255
water_pour = 0
for i in range(n):
    water = int(input())
    if capacity < water:
        print("Insufficient capacity!")
        continue
    else:
        water_pour += water
        capacity -= water
print(water_pour)
