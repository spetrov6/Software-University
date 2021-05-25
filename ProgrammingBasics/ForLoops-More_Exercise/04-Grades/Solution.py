students = int(input())
top_students = 0
four = 0
three = 0
fail = 0
total_grade = 0
for i in range(1, students + 1):
    grade = float(input())
    if grade >= 5.00:
        top_students += 1
    elif 4.00 <= grade <= 4.99:
        four += 1
    elif 3.00 <= grade <= 3.99:
        three += 1
    elif grade <= 2.99:
        fail += 1
    total_grade += grade
print(f"Top students: {top_students / students* 100:.2f}%")
print(f"Between 4.00 and 4.99: {four / students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {three / students * 100:.2f}%")
print(f"Fail: {fail / students * 100:.2f}%")
print(f"Average: {total_grade / students:.2f}")
