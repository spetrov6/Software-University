number_of_actions = int(input())
registered_peoples = {}
for _ in range(number_of_actions):
    action_as_list = input().split()
    action = action_as_list[0]
    name = action_as_list[1]
    if len(action_as_list) == 3:
        car_plate = action_as_list[2]
    if action == "register":
        if name in registered_peoples:
            print(f"ERROR: already registered with plate number {registered_peoples[name]}")
        else:
            registered_peoples[name] = car_plate
            print(f"{name} registered {car_plate} successfully")
    else:
        if name in registered_peoples:
            print(f"{name} unregistered successfully")
            registered_peoples.pop(name)
        else:
            print(f"ERROR: user {name} not found")
for key,value in registered_peoples.items():
    print(f"{key} => {value}")