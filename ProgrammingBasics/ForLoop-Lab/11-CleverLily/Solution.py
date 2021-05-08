n = int(input())
laundry = float(input())
toy_price = int(input())
toy = 0
money = 0
money_rd = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        toy += 1
    else:
        money_rd += 10
        money += money_rd - 1
money += toy * toy_price
if money >= laundry:
    print(f"Yes! {money - laundry:.2f}")
else:
    print(f"No! {laundry - money:.2f}")