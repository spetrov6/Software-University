first_words = list(map(lambda x: x,input().split(", ")))
second_words = list(map(lambda x: x,input().split(", ")))
substrings = [a for a in first_words for b in second_words if a in b]
print(sorted(set(substrings), key=substrings.index))