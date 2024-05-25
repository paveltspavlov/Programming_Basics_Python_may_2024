number = int(input())
points = 0
additional_points = 0

if number <= 100:
    points = 5
elif number > 100 and number < 1000:
    points = number * 0.2
elif number >= 1000:
    points = number * 0.1

if number % 2 == 0:
    additional_points = 1
elif number % 10 == 5:
    additional_points = 2

print(points + additional_points)
print(number + points + additional_points)
