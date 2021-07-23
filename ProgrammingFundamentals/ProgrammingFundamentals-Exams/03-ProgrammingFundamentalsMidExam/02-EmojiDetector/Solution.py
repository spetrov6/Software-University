import re,math
text = input()
pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"
numbers = [int(obj) for obj in re.findall(r"\d",text)]
thresh_hold = 1
for i in numbers:
    thresh_hold *= i
emojis = [obj.group() for obj in re.finditer(pattern,text)]
print(f"Cool threshold: {thresh_hold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in emojis:
    result = 0
    for letter in emoji:
        if letter.isalpha():
            result += ord(letter)
    if result >= thresh_hold:
        print(emoji)