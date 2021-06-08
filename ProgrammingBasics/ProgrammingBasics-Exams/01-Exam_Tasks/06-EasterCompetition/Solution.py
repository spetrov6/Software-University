bread = int(input())
points = 0
max_points = 0
winner = ""
for i in range(bread):
    cook = input()
    review = input()
    while review != "Stop":
        review_points = int(review)
        points += review_points
        review = input()
    print(f"{cook} has {points} points.")
    if points > max_points:
        max_points = points
        winner = cook
        print(f"{cook} is the new number 1!")
    points = 0
print(f"{winner} won competition with {max_points} points!")
