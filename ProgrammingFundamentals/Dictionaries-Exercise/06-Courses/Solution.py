course = input()
course_info = {}
while course != "end":
    course_name,student = course.split(" : ")
    if course_name not in course_info:
        course_info[course_name] = []
    course_info[course_name].append(student)
    course = input()
course_info = dict(sorted(course_info.items(),key=lambda kvp:len(kvp[1]),reverse=True))
for key,value in course_info.items():
    print(f"{key}: {len(course_info[key])}")
    for i in sorted(value):
        print(f"-- {i}")