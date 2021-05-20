chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
if season == "Spring" or season == "Summer":
    profit_chrysanthemums = chrysanthemums * 2.00
    profit_roses = roses * 4.10
    profit_tulips = tulips * 2.50
else:
    profit_chrysanthemums = chrysanthemums * 3.75
    profit_roses = roses * 4.50
    profit_tulips = tulips * 4.15
total_profit = profit_tulips + profit_roses + profit_chrysanthemums
if holiday == "Y":
    total_profit += total_profit * 0.15
if tulips >= 7 and season == "Spring":
    total_profit -= total_profit * 0.05
elif roses >= 10 and season == "Winter":
    total_profit -= total_profit * 0.10
if chrysanthemums + roses + tulips >= 20:
    total_profit -= total_profit * 0.20
print(f"{total_profit + 2:.2f}")