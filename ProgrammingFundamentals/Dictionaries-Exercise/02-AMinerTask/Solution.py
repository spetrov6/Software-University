resources = input()
resources_list = []
resources_dict = {}
while resources != "stop":
    resources_list.append(resources)
    resources = input()
for i in range(0,len(resources_list),2):
    res = resources_list[i]
    quantity = int(resources_list[i + 1])
    if res in resources_dict:
        resources_dict[res] += quantity
    else:
        resources_dict[res] = quantity
for resource,quantity in resources_dict.items():
    print(f"{resource} -> {quantity}")