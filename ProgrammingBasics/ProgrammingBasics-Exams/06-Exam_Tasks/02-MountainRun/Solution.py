record_seconds = float(input())
metres = float(input())
meter_second = float(input())
delay = (metres // 50) * 30
total_time = (metres * meter_second) + delay
if total_time < record_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {total_time - record_seconds:.2f} seconds slower.")