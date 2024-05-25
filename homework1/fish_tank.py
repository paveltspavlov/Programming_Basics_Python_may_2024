length = int(input())
width = int(input())
height = int(input())
percent = float(input())

total_volume = length * width * height
total_liters = float(total_volume / 1000)
needed_liters = float(total_liters * (1 - percent / 100))
print(needed_liters)
