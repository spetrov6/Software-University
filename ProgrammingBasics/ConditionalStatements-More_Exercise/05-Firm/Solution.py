from math import floor
hours_needed = int(input())
days_count = int(input())
days_left = days_count - (days_count * 0.10)
workers = int(input())
working_hours = days_left * 8
hours_overtime = workers * (days_count * 2)
total_hours = floor(working_hours + hours_overtime)
if total_hours >= hours_needed:
    print(f"Yes!{(total_hours - hours_needed)} hours left.")
else:
    print(f"Not enough time!{(hours_needed - total_hours)} hours needed.")
