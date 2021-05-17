from math import floor
from math import ceil
loze_area = int(input())
grape_count = float(input())
vine_needed = int(input())
workers = int(input())
grape_total = grape_count * loze_area
grape_vine = grape_total * 0.40
liters = grape_vine / 2.5

if liters < vine_needed:
    print(f"It will be a tough winter! More {floor(vine_needed - liters)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(liters)} liters.")
    print(f"{ceil(liters - vine_needed)} liters left -> {ceil((liters - vine_needed)/workers)} liters per person.")
