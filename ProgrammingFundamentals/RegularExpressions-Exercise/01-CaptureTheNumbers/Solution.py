import re
text = input()
result = []
pattern = r"\d+"
while not text == "":
    result.extend([obj.group() for obj in re.finditer(pattern,text)])
    text = input()
print(" ".join(result))