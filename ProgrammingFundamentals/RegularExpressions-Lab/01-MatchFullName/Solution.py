import re
names = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b",input())
print(" ".join(names))