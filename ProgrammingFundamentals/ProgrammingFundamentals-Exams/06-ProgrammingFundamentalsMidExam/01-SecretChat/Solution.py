message = input()
command = input()
while command != "Reveal":
    actions = command.split(":|:")
    if actions[0] == "InsertSpace":
        index = int(actions[1])
        first_part = message[:index]
        second_part = message[index:]
        message = first_part + " " + second_part
        print(message)
    elif actions[0] == "Reverse":
        if actions[1] in message:
            substring = actions[1][::-1]
            message = message.replace(actions[1],"",1)
            message = message + substring
            print(message)
        else:
            print("error")
    elif actions[0] == "ChangeAll":
        message = message.replace(actions[1],actions[2])
        print(message)
    command = input()
print(f"You have a new text message: {message}")