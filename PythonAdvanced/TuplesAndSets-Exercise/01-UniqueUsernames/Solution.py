names_count = int(input())
names = set([input() for _ in range(names_count)])
print("\n".join(names))