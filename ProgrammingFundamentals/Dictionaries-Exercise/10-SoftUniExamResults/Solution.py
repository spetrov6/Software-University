students_info_as_string = input()
languages = {}
students_points = {}
while students_info_as_string != "exam finished":
    if len(students_info_as_string.split("-")) > 2:
        student,language,points = students_info_as_string.split("-")
        if student not in students_points:
            students_points[student] = []
        students_points[student].append(int(points))
        if language not in languages:
            languages[language] = 0
        languages[language] += 1
    else:
        student = students_info_as_string.split("-")[0]
        students_points.pop(student)
    students_info_as_string = input()
students_points = sorted(students_points.items(),key=lambda kvp: (-max(kvp[1]),kvp[0]))
languages = sorted(languages.items(),key=lambda kvp: (-kvp[1],kvp[0]))
print("Results:")
for student in students_points:
    print(f"{student[0]} | {max(student[1])}")
print("Submissions:")
for submission in languages:
    print(f"{submission[0]} - {submission[1]}")
