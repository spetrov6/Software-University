exam_hour = int(input())
exam_minutes = int(input())
arrive_hour = int(input())
arrive_minutes = int(input())
exam_time = exam_hour * 60 + exam_minutes
arrive_time = arrive_hour * 60 + arrive_minutes
difference = abs(exam_time - arrive_time)
hh = difference // 60
mm = difference % 60
if exam_time >= arrive_time and difference <= 30:
    print("On time")
    if exam_time != arrive_time:
        print(f"{difference} minutes before the start")
elif exam_time > arrive_time and difference > 30:
    print("Early")
    if difference < 60:
        print(f"{difference} minutes before the start")
    else:
        print(f"{hh}:{mm:02d} hours before the start")
elif exam_time < arrive_time:
    print("Late")
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        print(f"{hh}:{mm:02d} hours after the start")