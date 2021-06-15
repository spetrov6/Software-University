nylon_needed = int(input())
paint_needed = int(input())
thinner_amount = int(input())
work_hours = int(input())
nylon_price = (nylon_needed + 2) * 1.50
paint_price = (paint_needed + (paint_needed * 0.10)) * 14.50
thinner_price = thinner_amount * 5
total_price = paint_price + nylon_price + thinner_price + 0.40
workers_profit = (total_price * 0.30) * work_hours
total_expences = workers_profit + total_price
print(f"Total expenses: {total_expences:.2f} lv.")