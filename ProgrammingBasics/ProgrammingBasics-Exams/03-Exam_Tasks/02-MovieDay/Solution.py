from math import floor
shoting_time = int(input())
stages_count = int(input())
stage_time = int(input())
time_for_shoting = stages_count * stage_time
preparation = shoting_time * 0.15
total_time = time_for_shoting + preparation
if total_time <= shoting_time:
    print(f"You managed to finish the movie on time! You have {round(shoting_time - total_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(total_time - shoting_time)} minutes.")