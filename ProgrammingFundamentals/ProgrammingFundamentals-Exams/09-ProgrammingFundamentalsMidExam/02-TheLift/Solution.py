people_count = int(input())
lift_list = [int(i) for i in input().split()]
for cabin in range(len(lift_list)):
    for places in range(people_count):
        if lift_list[cabin] < 4:
            lift_list[cabin] += 1
            people_count -= 1
        else:
            continue
if lift_list[-1] < 4:
    print("The lift has empty spots!")
elif lift_list[-1] == 4 and people_count > 0:
    print(f"There isn't enough space! {people_count} people in a queue!")
print(*lift_list,sep=" ")