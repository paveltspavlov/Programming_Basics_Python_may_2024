month = input()
nights = int(input())

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if nights > 7 and nights <= 14:
        studio = float(studio * 0.95)
    elif nights > 14:
        studio = float(studio * 0.7)
        apartment = float(apartment * 0.9)

elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        studio = float(studio * 0.8)
        apartment = float(apartment * 0.9)

elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if nights > 14:
        apartment = float(apartment * 0.9)

studio *= nights
apartment *= nights

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
