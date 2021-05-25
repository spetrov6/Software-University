cargo = int(input())
price = 0
load_total = 0
truck = 0
bus = 0
train = 0
for i in range(cargo):
    load = int(input())
    if load < 4:
        price += load * 200
        bus += load
    elif 4 <= load <= 11:
        price += load * 175
        truck += load
    elif load >= 12:
        price += load * 120
        train += load
    load_total += load
print(f"{price / load_total:.2f}")
print(f"{bus / load_total * 100:.2f}%")
print(f"{truck / load_total * 100:.2f}%")
print(f"{train / load_total * 100:.2f}%")