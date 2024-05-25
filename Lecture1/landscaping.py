yard_size = float(input())

price_per_meter = 7.61
final_price = yard_size * price_per_meter
discount = final_price * 0.18
final_price_with_discount = final_price - discount

print(f"The final price is: {final_price_with_discount} lv.")
print(f"The discount is: {discount} lv.")