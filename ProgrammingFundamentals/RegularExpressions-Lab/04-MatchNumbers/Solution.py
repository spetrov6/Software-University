import re
numbers = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
result = [obj.group() for obj in re.finditer(pattern,numbers)]
print(" ".join(result))