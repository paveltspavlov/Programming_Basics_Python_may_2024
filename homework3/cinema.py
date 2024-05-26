screening_type = input()
rows = int(input())
columns = int(input())
income = 0

cinema_capacity = rows * columns

if screening_type == "Premiere":
    income = float(cinema_capacity * 12)
elif screening_type == "Normal":
    income = float(cinema_capacity * 7.5)
elif screening_type == "Discount":
    income = float(cinema_capacity * 5)

print(f"{income:.2f} leva")
