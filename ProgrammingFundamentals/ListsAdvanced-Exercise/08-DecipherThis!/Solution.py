message = list(map(lambda x: x,input().split()))
decrypted_message = []
for i in message:
    ascii_character = ""
    character = []
    for j in i:
        if j.isdigit():
            ascii_character += j
        else:
            character += j
    character[0],character[-1] = character[-1],character[0]
    character = "".join(character)
    decrypted_message.append(chr(int(ascii_character))+character)
print(*decrypted_message,sep=" ")

