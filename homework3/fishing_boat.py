budget = int(input())
season = input()
number_of_fishermen = int(input())

final_rent = 0

if season == "Spring":
    rent = 3000
    if number_of_fishermen <= 6:
        final_rent = float(rent * 0.9)
    elif number_of_fishermen >= 7 and number_of_fishermen <= 11:
        final_rent = float(rent * 0.85)
    elif number_of_fishermen >= 12:
        final_rent = float(rent * 0.75)
elif season == "Summer" or season == "Autumn":
    rent = 4200
    if number_of_fishermen <= 6:
        final_rent = float(rent * 0.9)
    elif number_of_fishermen >=7 and number_of_fishermen <= 11:
        final_rent = float(rent * 0.85)
    elif number_of_fishermen >= 12:
        final_rent = float(rent * 0.75)
elif season == "Winter":
    rent = 2600
    if number_of_fishermen <= 6:
        final_rent = float(rent * 0.9)
    elif number_of_fishermen >= 7 and number_of_fishermen <= 11:
        final_rent = float(rent * 0.85)
    elif number_of_fishermen >= 12:
        final_rent = float(rent * 0.75)



if number_of_fishermen % 2 == 0 and season != "Autumn":
    final_rent *= 0.95

if budget >= final_rent:
    print(f"Yes! You have {budget - final_rent:.2f} leva left.")
else:
    print(f"Not enough money! You need {final_rent - budget:.2f} leva.")
