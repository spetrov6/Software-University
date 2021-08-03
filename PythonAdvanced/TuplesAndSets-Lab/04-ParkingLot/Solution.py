commands_count = int(input())
in_set = set()
for _ in range(commands_count):
    comm,num = input().split(", ")
    if comm == "IN":
        in_set.add(num)
    else:
        in_set.remove(num)

if in_set:
    [print(x) for x in in_set]
else:
    print("Parking Lot is Empty")