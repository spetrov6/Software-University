offers_list = input().split(sep=", ")
beggar_count = int(input())
home = []
numbers_list = []
counter = 0
for i in range(beggar_count):
    home.append(0)
for i in offers_list:
    numbers_list.append(int(i))
while len(numbers_list) > counter:
    for i in range(beggar_count):
        if counter < len(numbers_list):
            home[i] += numbers_list[counter]
            counter += 1
        else:
            break
print(home)
