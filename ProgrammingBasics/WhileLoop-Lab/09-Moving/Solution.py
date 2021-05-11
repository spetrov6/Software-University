width = int(input())
length = int(input())
height = int(input())
size = width * length * height
box = input()
free_space = size
while box != "Done":
    free_space = free_space - int(box)
    if free_space <= 0:
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        break
    box = input()
if free_space > 0:
    print(f"{abs(free_space)} Cubic meters left.")