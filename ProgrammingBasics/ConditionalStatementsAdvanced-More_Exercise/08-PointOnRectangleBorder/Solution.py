x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())
firstcondition = bool((x == x1 or x == x2) and (y1 <= y <= y2))
secondcondition = bool((y == y1 or y == y2) and (x1 <= x <= x2))
if firstcondition or secondcondition:
    print("Border")
else:
    print("Inside / Outside")
