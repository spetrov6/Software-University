import sys
n = int(input())
max_even = -sys.maxsize
min_even = sys.maxsize
min_odd = sys.maxsize
max_odd = -sys.maxsize
sum_odd = 0
sum_even = 0
for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 0:
       if num > max_even:
           max_even = num
       if num < min_even:
           min_even = num
       sum_even += num

    elif i % 2 != 0:
        if num > max_odd:
            max_odd = num
        if num < min_odd:
            min_odd = num
        sum_odd += num

if n == 0:
   print("OddSum=0.00,")
   print("OddMin=No,")
   print("OddMax=No,")
   print("EvenSum=0.00,")
   print("EvenMin=No,")
   print("EvenMax=No")
elif n == 1:
    print(f"OddSum={sum_odd:.2f},")
    print(f"OddMin={min_odd:.2f},")
    print(f"OddMax={max_odd:.2f},")
    print("EvenSum=0.00,")
    print("EvenMin=No,")
    print("EvenMax=No")
else:
   print(f"OddSum={sum_odd:.2f},")
   print(f"OddMin={min_odd:.2f},")
   print(f"OddMax={max_odd:.2f},")
   print(f"EvenSum={sum_even:.2f},")
   print(f"EvenMin={min_even:.2f},")
   print(f"EvenMax={max_even:.2f}")