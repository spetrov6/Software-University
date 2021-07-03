key = int(input())
n = int(input())
word = ""
for i in range(n):
    letter = input()
    letter = ord(letter) + key
    word += chr(letter)
print(word)
