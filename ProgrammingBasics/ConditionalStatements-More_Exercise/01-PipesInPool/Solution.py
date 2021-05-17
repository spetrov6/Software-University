v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())
p1_liters = p1 * h
p2_liters = p2 * h
litres = p1_liters + p2_liters
ephtines = (litres / v) * 100
if litres <= v:
    print(f"The pool is {ephtines:.2f} full. Pipe 1: {(p1_liters / litres) * 100:.2f}%. Pipe 2: {(p2_liters / litres) * 100:.2f}%.")
else:
    print(f"For {h} hours the pool overflows with {litres - v:.2f} liters.")


