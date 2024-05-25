from math import ceil

tv_series = input()
episode_length = int(input())
lunch_break_duration = int(input())

time_to_eat = lunch_break_duration / 8
time_to_relax = lunch_break_duration / 4
time_left = lunch_break_duration - time_to_eat - time_to_relax

if episode_length <= time_left:
    final_time = ceil(time_left - episode_length)
    print(f"You have enough time to watch {tv_series} and left with {final_time} minutes free time.")

elif episode_length > time_left:
    final_time = ceil(episode_length - time_left)
    print(f"You don't have enough time to watch {tv_series}, you need {final_time} more minutes.")
