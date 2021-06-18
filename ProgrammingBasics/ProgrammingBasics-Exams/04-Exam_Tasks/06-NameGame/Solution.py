name = input()
points = 0
max_points = 0
winner = ""
while name != "Stop":
    for i in name:
        number = int(input())
        if number == ord(i):
            points += 10
        else:
            points += 2
    if points >= max_points:
        max_points = points
        winner = name
    points = 0
    name = input()
print(f"The winner is {winner} with {max_points} points!")