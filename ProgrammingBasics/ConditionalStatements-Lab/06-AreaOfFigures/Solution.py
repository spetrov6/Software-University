tour_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
toys_seled = puzzles + dolls + bears + minions + trucks
puzzle_earnings = puzzles * 2.60
doll_earnings = dolls * 3
bear_earnings = bears * 4.10
minion_earnings = minions * 8.20
truck_earnings = trucks * 2
profit = puzzle_earnings + doll_earnings + bear_earnings + minion_earnings + truck_earnings
discount = profit * 0.25
rent = profit * 0.10
if toys_seled >= 50:
    rent = 0.10 * (profit - discount)
    total_profit = profit - rent - discount
else:
    total_profit = profit - rent
if total_profit >= tour_price:
    print(f"Yes! {total_profit - tour_price:0.2f} lv left.")
else:
    print(f"Not enough money! {tour_price - total_profit:0.2f} lv needed.")
