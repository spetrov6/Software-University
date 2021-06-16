budget = float(input())
GPU = int(input())
CPU = int(input())
RAM = int(input())
GPU_price = GPU * 250
CPU_price = (GPU_price * 0.35) * CPU
RAM_price = (GPU_price * 0.10) * RAM
total = GPU_price + CPU_price + RAM_price
if GPU > CPU:
    total -= total * 0.15
if budget >= total:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")