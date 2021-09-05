elements_count = int(input())
set_of_elements = set()
for _ in range(elements_count):
    elements = input().split()
    for el in elements:
        set_of_elements.add(el)
[print(x) for x in set_of_elements]