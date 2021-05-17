free = int(input())
working = 365 - free
free_play = free * 127
working_play = working * 63
total_play = free_play + working_play
if total_play <= 30000:
    print("Tom sleeps well")
    total_play = 30000 - total_play
    print(f"{total_play // 60} hours and {total_play % 60} minutes less for play")
else:
    print("Tom will run away")
    total_play = total_play - 30000
    print(f"{total_play // 60} hours and {total_play % 60} minutes more for play")
