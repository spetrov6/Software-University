from math import floor
hour = int(input())
minutes = int(input()) + 15

if minutes >= 60:
    hour = hour + 1
    minutes = 0 + (minutes%15)
minutes = floor(minutes)

if hour >= 24:
    hour = 0
if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")