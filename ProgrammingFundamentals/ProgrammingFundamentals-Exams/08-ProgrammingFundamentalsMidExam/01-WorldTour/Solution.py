stops = input()
command = input()
while command != "Travel":
    activity = command.split(":")
    if activity[0] == "Add Stop":
        if 0 <= int(activity[1]) < len(stops):
            first_part = stops[:int(activity[1])]
            second_part = stops[int(activity[1]):]
            stops = first_part + activity[2] + second_part
    elif activity[0] == "Remove Stop":
        if 0 <= int(activity[1]) < len(stops) and 0 <= int(activity[2]) < len(stops):
            first_part = stops[:int(activity[1])]
            second_part = stops[int(activity[2]) + 1:]
            stops = first_part + second_part
    elif activity[0] == "Switch":
        old_string,new_string = activity[1],activity[2]
        if old_string in stops:
            stops = stops.replace(old_string,new_string)
    print(stops)
    command = input()
print(f"Ready for world tour! Planned stops: {stops}")