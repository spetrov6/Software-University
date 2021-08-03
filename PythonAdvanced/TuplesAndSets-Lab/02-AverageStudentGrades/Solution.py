students_count = int(input())
students = {}
for _ in range(students_count):
    student,grade = input().split()
    if student not in students:
        students[student] = []
    students[student].append(float(grade))
for key,value in students.items():
    print(f"{key} -> {' '.join([f'{x:.2f}' for x in value])} (avg: {sum(value) / len(value):.2f})")