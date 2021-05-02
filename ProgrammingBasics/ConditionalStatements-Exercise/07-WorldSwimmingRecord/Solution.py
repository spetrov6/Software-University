from math import floor
world_record = float(input())
metres = float(input())
athlete_seconds_for_1m = float(input()) * metres

delay = floor(metres / 15) * 12.5
athlete_time = athlete_seconds_for_1m + delay


if athlete_time < world_record:
    print(f"Yes, he succeeded! The new world record is {athlete_time:0.2f} seconds.")
else:
    print(f"No, he failed! He was {athlete_time - world_record:0.2f} seconds slower.")