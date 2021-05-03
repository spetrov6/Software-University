years = float(input())
gander = input()

if gander == "m":
  if years < 16:
      print("Master")
  else:
      print("Mr.")
elif gander == "f":
    if years < 16:
        print("Miss")
    else:
        print("Ms.")