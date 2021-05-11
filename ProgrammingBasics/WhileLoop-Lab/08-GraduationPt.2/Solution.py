name = input()
classe = 1
total = 0
last_grade = 0
while classe <= 12:
    classe += 1
    grade = float(input())
    if grade < 4.00:
        if last_grade !=0 and last_grade < 4.00:
            print(f"{name} has been excluded at {classe} grade")
            break
        classe -= 2
    last_grade = grade
    total += grade
    if classe > 12:
        print(f"{name} graduated. Average grade: {total / (classe - 1):.2f}")