rent = int(input())
figure_price = rent - (rent * 0.30)
food_price = figure_price - (figure_price * 0.15)
sound = food_price / 2
total = rent + food_price + figure_price + sound
print(f"{total:.2f}")