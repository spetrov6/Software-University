first = input()
second = input()
third = input()
win = 0
draw = 0
lose = 0
if first[0] > first[2]:
    win += 1
elif first[0] == first[2]:
    draw += 1
elif first[0] < first[2]:
    lose += 1
if second[0] > second[2]:
    win += 1
elif second[0] == second[2]:
    draw += 1
elif second[0] < second[2]:
    lose += 1
if third[0] > third[2]:
    win += 1
elif third[0] == third[2]:
    draw += 1
elif third[0] < third[2]:
    lose += 1
print(f"Team won {win} games.")
print(f"Team lost {lose} games.")
print(f"Drawn games: {draw}")