from math import ceil
series = input()
episode_time = int(input())
lunch_time = int(input())
lunch = lunch_time / 8
relax = lunch_time / 4
time_left = lunch_time - lunch - relax
if time_left >= episode_time:
    print(f"You have enough time to watch {series} and left with {ceil(time_left - episode_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(episode_time - time_left)} more minutes.")
