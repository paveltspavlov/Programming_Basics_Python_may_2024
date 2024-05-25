hours = int(input())
minutes = int(input())

buff_tine = 15

if (minutes + 15) <= 59:
    minutes = minutes + 15
elif (minutes + 15) > 59:
    minutes = minutes + 15 - 60
    hours += 1

if minutes < 10:
    minutes = f"0{minutes}"
elif minutes >= 10:
    minutes = f"{minutes}"
if hours > 23:
    hours = 0

print(f"{hours}:{minutes}")