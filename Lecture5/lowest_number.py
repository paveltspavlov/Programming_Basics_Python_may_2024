number = input()
min_number = 1000000000000

while number != "Stop":
    number = int(number)
    if number < min_number:
        min_number = number
    number = input()

print(f"{min_number:.0f}")
