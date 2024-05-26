flower_type = input()
flower_count = int(input())
budget = int(input())
final_price = float(0)
if flower_type == "Roses":
    price = 5
    if flower_count > 80:
        final_price = float(price * flower_count) * 0.9
    else:
        final_price = float(price * flower_count)
elif flower_type == "Dahlias":
    price = 3.8
    if flower_count > 90:
        final_price = float(price * flower_count) * 0.85
    else:
        final_price = float(price * flower_count)
elif flower_type == "Tulips":
    price = 2.8
    if flower_count > 80:
        final_price = float(price * flower_count) * 0.85
    else:
        final_price = float(price * flower_count)
elif flower_type == "Narcissus":
    price = 3
    if flower_count < 120:
        final_price = float(price * flower_count) * 1.1
    else:
        final_price = float(price * flower_count)
elif flower_type == "Gladiolus":
    price = 2.5
    if flower_count < 80:
        final_price = float(price * flower_count) * 1.2
    else:
        final_price = float(price * flower_count)


if final_price > budget:
    difference = float(final_price - budget)
    print(f"Not enough money, you need {difference:.2f} leva more.")
elif final_price <= budget:
    difference = float(budget - final_price)
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {difference:.2f} leva left.")
