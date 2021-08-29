string = input()
encrypted_string = ""
for character in string:
    encrypted_string += chr(ord(character) + 3)
print(encrypted_string)