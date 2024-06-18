num_of_tournaments = int(input())

initial_points = int(input())

points = 0
number_of_wins = 0

for i in range(num_of_tournaments):
    place = input()
    if place == "W":
        points += 2000
        number_of_wins += 1
    elif place == "F":
        points += 1200
    elif place == "SF":
        points += 720
    i += i

percentage_of_wins = (number_of_wins  /num_of_tournaments) * 100
average_points = points / num_of_tournaments

print(f"Final points: {initial_points + points}")
print(f"Average points: {int(average_points)}")
print(f"{percentage_of_wins:.2f}%")
