from math import floor

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time // 60
seconds = total_time % 60
minutes = floor(minutes)

if seconds < 10 and minutes < 10:
    print(f"{minutes}:0{seconds}")
elif seconds < 10 and minutes >= 10 and minutes <=60:
    print(f"{minutes}:0{seconds}")
elif seconds >= 10:
    print(f"{minutes}:{seconds}")
