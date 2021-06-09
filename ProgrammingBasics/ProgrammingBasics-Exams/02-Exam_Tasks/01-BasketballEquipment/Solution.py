tax = int(input())
sneakers = tax - (tax * 0.40)
outfit = sneakers - (sneakers * 0.20)
ball = outfit / 4
accessories = ball / 5
total = tax + sneakers + outfit + ball + accessories
print(f"{total:.2f}")