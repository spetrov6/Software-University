name = input()
days = int(input())
tickets_count = int(input())
ticket_price = float(input())
cinema_percents = int(input()) / 100
ticket_total = days * tickets_count
profit = ticket_total * ticket_price
profit_cinema = profit * cinema_percents
print(f"The profit from the movie {name} is {profit - profit_cinema:.2f} lv.")

