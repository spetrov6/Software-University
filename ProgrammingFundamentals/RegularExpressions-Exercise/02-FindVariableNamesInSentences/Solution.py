import re
text = input()
pattern = r"\b_([a-zA-Z0-9]+)\b"
result = [obj for obj in re.findall(pattern,text)]
print(",".join(result))