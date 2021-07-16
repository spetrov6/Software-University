elements = input().split()
elements_dict = {}
for i in range(0,len(elements),2):
    key = elements[i]
    value = elements[i + 1]
    elements_dict[key] = int(value)
print(elements_dict)