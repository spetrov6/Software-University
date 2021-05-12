width = int(input())
length = int(input())
cake_size = width * length
cake_left = cake_size
piece_taken = input()
while piece_taken != "STOP":
    cake_left = cake_left - int(piece_taken)
    if cake_left <= 0:
        print(f"No more cake left! You need {abs(cake_left)} pieces more.")
        break
    piece_taken = input()
if cake_left > 0:
    print(f"{cake_left} pieces are left.")