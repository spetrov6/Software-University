number_of_rows = int(input())
students_info = {}
average_students = {}
for _ in range(number_of_rows):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_info:
        students_info[student_name] = []
    students_info[student_name].append(student_grade)
for student,grade in students_info.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        average_students[student] = average_grade
print("\n".join([f"{i[0]} -> {i[1]:.2f}" for i in sorted(average_students.items(),key=lambda kvm:-kvm[1])]))