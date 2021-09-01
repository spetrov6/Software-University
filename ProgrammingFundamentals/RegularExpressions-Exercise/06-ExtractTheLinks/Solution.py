import re
text = input()
pattern = r"www\.[a-zA-Z0-9]+(-[a-z0-9]+)*\.[a-z]+(\.[a-z]+)*"
result = []
while text != "":
    result.extend([obj.group() for obj in re.finditer(pattern, text)])
    text = input()
print('\n'.join(result))