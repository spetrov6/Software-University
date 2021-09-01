import re
text = input()
pattern = r"(?<=\s)[a-z0-9]+((\.|-|_)[a-z0-9]+)?@[a-z0-9]+((\.|-|_)[a-z0-9]+)?\.[a-z0-9]+(\.[a-z0-9]+)?"
result = [obj.group() for obj in re.finditer(pattern,text,re.IGNORECASE)]
print("\n".join(result))