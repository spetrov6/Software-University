password = input()
command = input()
while command != "Done":
    action = command.split()
    if action[0] == "TakeOdd":
        password = password[1::2]
        print(password)
    elif action[0] == "Cut":
        index,length = int(action[1]),int(action[2])
        substring = password[index:index + length]
        password = password.replace(substring,"",1)
        print(password)
    elif action[0] == "Substitute":
        substring,substitute = action[1],action[2]
        if substring in password:
            password = password.replace(substring,substitute)
            print(password)
        else:
            print(f"Nothing to replace!")
    command = input()
print(f"Your password is: {password}")