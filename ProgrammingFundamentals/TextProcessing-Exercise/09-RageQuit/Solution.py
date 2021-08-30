message = list(input().upper())
unique_chars = set()
rage_message =""
characters = ""
for index in range(len(message)):
    if message[index].isdigit():
        if index < len(message) - 1 and message[index + 1].isdigit():
            multiplayer = message[index] + message[index + 1]
            rage_message += characters * int(multiplayer)
            characters = ""
        else:
            rage_message += characters * int(message[index])
            characters = ""
    else:
        characters += message[index]
        unique_chars.add(message[index])
print(f"Unique symbols used: {len(unique_chars)}")
print(rage_message)