tarp = int(input())
liters_of_paint_needed = int(input())
paint_thinner = int(input())
hours_needed = int(input())

#tarp + 2 sq meters
tarp_price = float((tarp+2) * 1.5)

paint_price = float(liters_of_paint_needed * 14.5)

#paint + 10%
total_paint = float(paint_price*1.1)

paint_thinner_price = float(paint_thinner * 5)
plastic_bags_price = float(0.4)

total_price = float(plastic_bags_price + tarp_price + total_paint + paint_thinner_price)
workers_salary = float((total_price * 0.3) * hours_needed)
total_cost = float(total_price + workers_salary)

print(total_cost)
