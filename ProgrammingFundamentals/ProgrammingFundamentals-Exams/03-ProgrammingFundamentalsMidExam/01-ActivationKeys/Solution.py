activation_key = input()
command = input()
while command != "Generate":
    actions = command.split(">>>")
    if actions[0] == "Contains":
        substring = actions[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif actions[0] == "Flip":
        start,end = int(actions[2]),int(actions[3])
        first_part = activation_key[:start]
        second_part = activation_key[end:]
        substring = activation_key[start:end]
        if actions[1] == "Upper":
            substring = substring.upper()
        else:
            substring = substring.lower()
        activation_key = first_part + substring + second_part
        print(activation_key)
    elif actions[0] == "Slice":
        start,end = int(actions[1]),int(actions[2])
        first_part = activation_key[:start]
        second_part = activation_key[end:]
        activation_key = first_part + second_part
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")