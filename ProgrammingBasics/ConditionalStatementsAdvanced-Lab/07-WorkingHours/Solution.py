hour = int(input())
day = input()
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
if day in working_days and hour >= 10 and hour <= 18:
      print("open")
else:
    print("closed")