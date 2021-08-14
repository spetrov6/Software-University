fires_list = input().split("#")
water = int(input())
effort = 0
fire_power = 0
cell_saved = []
total_fire = 0
for index in range(len(fires_list)):
    fires_list[index] = fires_list[index].split(" = ")
    fire_power = int(fires_list[index][1])
    if water >= fire_power:
        if fires_list[index][0] == "High" and 81 <= fire_power <= 125:
            water -= fire_power
            effort += fire_power * 0.25
            cell_saved.append(" - " + str(fire_power))
            total_fire += fire_power
        elif fires_list[index][0] == "Medium" and 51 <= fire_power <= 80:
            water -= fire_power
            effort += fire_power * 0.25
            cell_saved.append(" - " + str(fire_power))
            total_fire += fire_power
        elif fires_list[index][0] == "Low" and 1 <= fire_power <= 50:
            water -= fire_power
            effort += fire_power * 0.25
            cell_saved.append(" - " + str(fire_power))
            total_fire += fire_power
print("Cells:")
for i in cell_saved:
    print(i)
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")