budget = float(input())
season = input()

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
        place_to_stay = "Camp"
    elif season == "winter":
        price = budget * 0.7
        place_to_stay = "Hotel"
if budget > 100 and budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
        place_to_stay = "Camp"
    elif season == "winter":
        price = budget * 0.8
        place_to_stay = "Hotel"
if budget > 1000:
    destination = "Europe"
    price = budget * 0.9
    place_to_stay = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place_to_stay} - {price:.2f}")
