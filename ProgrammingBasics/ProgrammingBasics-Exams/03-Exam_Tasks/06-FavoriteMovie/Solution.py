import sys
command = input()
count = 0
max_point = -sys.maxsize
best_movie = ""
points = 0
while command != "STOP":
    count += 1
    lenth = len(command)
    for i in command:
        points += ord(i)
        letter = ord(i)
        if letter >= 65 and letter <= 90:
            points -= lenth
        elif letter > 90:
            points -= (lenth * 2)
    if points > max_point:
        best_movie = command
        max_point = points
    points = 0
    if count >= 7:
        print("The limit is reached.")
        break
    command = input()
print(f"The best movie for you is {best_movie} with {max_point} ASCII sum.")