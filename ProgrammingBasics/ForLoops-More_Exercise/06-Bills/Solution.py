month = int(input())
water = 20
water_total = 0
internet = 15
internet_total = 0
electricity_total = 0
electricity = 0
other_total = 0
for i in range(1,month + 1):
    electricity = float(input())
    electricity_total += electricity
    water_total += water
    internet_total += internet
    bill = water + electricity + internet
    other = bill + (bill * 0.20)
    other_total += other
total = electricity_total + internet_total  + water_total + other_total
print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water_total:.2f} lv")
print(f"Internet: {internet_total:.2f} lv")
print(f"Other: {other_total:.2f} lv")
print(f"Average: {total / month:.2f} lv")