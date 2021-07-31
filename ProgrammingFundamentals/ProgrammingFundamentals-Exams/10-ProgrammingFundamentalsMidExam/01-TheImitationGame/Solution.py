message = input()
command = input()
while command != "Decode":
    actions = command.split("|")
    if actions[0] == "Move":
        first_part = message[:int(actions[1])]
        last_part = message[int(actions[1]):]
        message = last_part + first_part
    elif actions[0] == "Insert":
        first_part = message[:int(actions[1])]
        last_part = message[int(actions[1]):]
        message = first_part + actions[2] + last_part
    elif actions[0] == "ChangeAll":
        message = message.replace(actions[1],actions[2])
    command = input()
print(f"The decrypted message is: {''.join(message)}")