import re
names = input()
result = [obj.group() for obj in re.finditer(r"\+359( |-)2\1\d{3}\1\d{4}\b",names)]
print(", ".join(result))