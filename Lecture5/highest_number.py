number = input()
max_number = -1000000000000

while number != "Stop":
    number = int(number)
    if number > max_number:
        max_number = number
    number = input()

print(f"{max_number:.0f}")
