pens = int(input())
markers = int(input())
cleaning = float(input())
discount_percent = float(input()) * 0.01
pens_money = pens * 5.80
markers_money = markers * 7.20
cleaning_money = cleaning * 1.20
total = pens_money + markers_money + cleaning_money
discount = total * discount_percent
print(f"{total - discount:.3f}")