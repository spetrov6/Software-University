jury_count = int(input())
presentation = input()
presentation_count = 0
presentation_grade = 0
grades = 0
grade_total = 0
while presentation != "Finish":
    for i in range(jury_count):
        grade = float(input())
        grades += grade
    grade_total = grades / jury_count
    print(f"{presentation} - {grade_total:.2f}.")
    presentation_grade += grade_total
    grades = 0
    presentation_count += 1
    presentation = input()
print(f"Student's final assessment is {presentation_grade / presentation_count:.2f}.")

