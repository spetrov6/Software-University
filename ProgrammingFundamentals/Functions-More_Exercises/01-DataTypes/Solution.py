def data_types(comm,item):
    if comm == "int":
        print(int(item) * 2)
    elif comm == "real":
        print(f"{float(item) * 1.5:.2f}")
    else:
        print(f"${item}$")
command = input()
item_argument = input()
data_types(command,item_argument)
