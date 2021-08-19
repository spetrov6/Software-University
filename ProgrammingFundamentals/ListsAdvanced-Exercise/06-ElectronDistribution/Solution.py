electrons = int(input())
shells = []
shell = 1
while electrons > 0:
    if electrons > 2 * shell ** 2:
        shells.append(2 * shell ** 2)
        electrons -= 2 * shell ** 2
    else:
        shells.append(electrons)
        electrons -= electrons
    shell += 1
print(shells)