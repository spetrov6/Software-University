from math import ceil
peoples_count = int(input())
price = float(input())
sunbed_price = float(input())
umbrella_price =float(input())
unbrella_count = ceil(peoples_count / 2)
sunbed_count = ceil(peoples_count - (peoples_count * 0.25))
unbrella_total = umbrella_price * unbrella_count
sunbed_total = sunbed_count * sunbed_price
price_enter = peoples_count * price
total = price_enter + unbrella_total + sunbed_total
print(f"{total:.2f} lv.")