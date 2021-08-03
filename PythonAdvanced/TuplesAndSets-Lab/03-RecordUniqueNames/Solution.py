peoples_count = int(input())
peoples = set()
for _ in range(peoples_count):
    peoples.add(input())
[print(x) for x in peoples]
