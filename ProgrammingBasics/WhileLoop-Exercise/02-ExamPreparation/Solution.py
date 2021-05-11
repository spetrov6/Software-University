bad_grades_total = int(input())
bad_grades_count = 0
command = input()
command_count = 0
total = 0
while command != "Enough":
    last_command = command
    grade = int(input())
    if grade <= 4:
        bad_grades_count += 1
        if bad_grades_count >= bad_grades_total:
            print(f"You need a break, {bad_grades_count} poor grades.")
            break
    total += grade
    command_count += 1
    command = input()
if command == "Enough":
    print(f"Average score: {total / command_count:.2f}")
    print(f"Number of problems: {command_count}")
    print(f"Last problem: {last_command}")
