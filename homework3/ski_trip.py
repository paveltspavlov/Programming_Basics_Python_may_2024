days_to_stay = int(input())
room_type = input()
review = input()

room_for_one = 18.00
apartment = 25.00
president_apartment = 35.00

nights_to_stay = days_to_stay - 1

if room_type == "room for one person":
    total_price = nights_to_stay * room_for_one
elif room_type == "apartment":
    if days_to_stay < 10:
        total_price = float((nights_to_stay * apartment) * 0.9)
    elif days_to_stay >= 10 and days_to_stay <= 15:
        total_price = float((nights_to_stay * apartment) * 0.65)
    elif days_to_stay > 15:
        total_price = float((nights_to_stay * apartment) * 0.5)
elif room_type == "president apartment":
    if days_to_stay < 10:
        total_price = float((nights_to_stay * president_apartment) * 0.9)
    elif days_to_stay >= 10 and days_to_stay <= 15:
        total_price = float((nights_to_stay * president_apartment) * 0.85)
    elif days_to_stay > 15:
        total_price = float((nights_to_stay * president_apartment) * 0.8)


if review == "positive":
   total_price = float(total_price * 1.25)
else:
   total_price = float(total_price * 0.9)


print(f"{total_price:.2f}")
