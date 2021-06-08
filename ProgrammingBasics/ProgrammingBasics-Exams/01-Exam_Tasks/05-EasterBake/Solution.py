from math import ceil
bread = int(input())
flour_max = 0
sugar_max = 0
sugar_total = 0
flour_total = 0
for i in range(bread):
    sugar = int(input())
    flour = int(input())
    sugar_total += sugar
    flour_total += flour
    if flour > flour_max:
        flour_max = flour
    if sugar > sugar_max:
        sugar_max = sugar
print(f"Sugar: {ceil(sugar_total / 950)}")
print(f"Flour: {ceil(flour_total / 750)}")
print(f"Max used flour is {flour_max} grams, max used sugar is {sugar_max} grams.")