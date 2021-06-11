from math import floor
series = input()
seasons = int(input())
episodes = int(input())
episode_time = float(input())
episodes_time_total = (seasons * episodes) * episode_time
ad = episodes_time_total * 0.20
total_time = episodes_time_total + ad + (seasons * 10)
print(f"Total time needed to watch the {series} series is {floor(total_time)} minutes.")
