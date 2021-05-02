from math import floor
racer1 = int(input())
racer2 = int(input())
racer3 = int(input())
time = racer1 + racer2 + racer3
minute = time / 60
second = time % 60
minute = floor(minute)
if second < 10:
   print(f"{minute}:0{second}")
else:
   print(f"{minute}:{second}")
