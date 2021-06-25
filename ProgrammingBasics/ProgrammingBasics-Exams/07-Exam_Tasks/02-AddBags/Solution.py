price_baggage_over_20kg = float(input())
baggage_kilograms = float(input())
days_to_flight = int(input())
baggage_count = int(input())
total_price = 0
if baggage_kilograms < 10:
    total_price += price_baggage_over_20kg * 0.20
elif 10 <= baggage_kilograms <= 20:
    total_price += price_baggage_over_20kg * 0.50
else:
    total_price += price_baggage_over_20kg
if days_to_flight > 30:
    total_price += total_price * 0.10
elif 7 <= days_to_flight <= 30:
    total_price += total_price * 0.15
else:
    total_price += total_price * 0.40
total_price *= baggage_count
print(f"The total price of bags is: {total_price:.2f} lv.")
