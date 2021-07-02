n = int(input())
for num in range(1,n + 1):
  num_sum = 0
  num_obj = str(num)
  for obj in num_obj:
      num_sum += int(obj)
  if num_sum == 5 or num_sum == 7 or num_sum == 11:
      print(f"{num} -> True")
  else:
      print(f"{num} -> False")