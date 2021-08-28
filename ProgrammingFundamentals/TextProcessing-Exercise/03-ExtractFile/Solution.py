path = input().split("\\")
file = path[-1]
file = file.split(".")
print(f"File name: {file[0]}\nFile extension: {file[1]}")