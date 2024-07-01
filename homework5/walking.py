goal = 10000
steps = 0
command = ""

while command != "Going home":
    command = input()
    if command == "Going home":
        break
    steps += int(command)

    if steps >= goal:
        print("Goal reached! Good job!")
        print(f"{steps - goal} steps over the goal!")
        break
    elif steps < goal:
        continue

if command == "Going home":
    steps += int(input())
    if steps < goal:
        print(f"{goal - steps} more steps to reach goal.")
    else:
        print("Goal reached! Good job!")
        print(f"{steps - goal} steps over the goal!")
