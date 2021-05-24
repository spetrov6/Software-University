money = float(input())
final_year = int(input())
money_needed = 0
years = 18
for i in range(1800,final_year + 1):
    if i % 2 == 0:
        money_needed += 12000
    else:
        money_needed += 12000 + (50 * years)
    years += 1
if money >= money_needed:
    print(f"Yes! He will live a carefree life and will have {money - money_needed:.2f} dollars left.")
else:
    print(f"He will need {money_needed - money:.2f} dollars to survive.")
