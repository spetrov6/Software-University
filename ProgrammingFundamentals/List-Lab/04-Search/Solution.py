n = int(input())
word = input()
list_all = []
list_including = []
for i in range(n):
    sentence = input()
    list_all.append(sentence)
for j in list_all:
    if word in j:
        list_including.append(j)
print(list_all)
print(list_including)