movie = input()
food = input()
tickets = int(input())
ticket_price = 0
if movie == "John Wick":
    if food == "Drink":
        ticket_price = 12
    elif food == "Popcorn":
        ticket_price = 15
    else:
        ticket_price = 19
elif movie == "Star Wars":
    if food == "Drink":
        ticket_price = 18
    elif food == "Popcorn":
        ticket_price = 25
    else:
        ticket_price = 30
else:
    if food == "Drink":
        ticket_price = 9
    elif food == "Popcorn":
        ticket_price = 11
    else:
        ticket_price = 14
total_price = ticket_price * tickets
if movie == "Star Wars" and tickets >= 4:
    discount = total_price * 0.30
    total_price -= discount
elif movie == "Jumanji" and tickets == 2:
    discount = total_price * 0.15
    total_price -= discount
print(f"Your bill is {total_price:.2f} leva.")

