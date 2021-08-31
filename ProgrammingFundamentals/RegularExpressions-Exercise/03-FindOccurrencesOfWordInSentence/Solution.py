import re
text = input()
word = input()
pattern = fr"\b{word}\b"
result = [obj for obj in re.findall(pattern,text,re.IGNORECASE)]
print(len(result))