number_of_pen_packages = int(input())
number_of_marker_packages = int(input())
liters_of_detergent = float(input())
discount = int(input())

pricec_for_pens = float(number_of_pen_packages * 5.80)
price_for_markers = float(number_of_marker_packages * 7.20)
price_for_detergent = float(liters_of_detergent * 1.20)
total_price = price_for_markers + pricec_for_pens + price_for_detergent
discount = total_price * (discount / 100)
final_price = total_price - discount

print(final_price)
