lily_age = int(input())
washer_price = float(input())
toy_price = int(input())

money_saved = 0
toys = 0
money_taken = 1
i = 0
buff1 = 10

for i in range(1, lily_age + 1):
    if i % 2 == 0:
        money_saved += buff1
        money_saved -= 1
        money_taken += 1
        buff1 += 10
    else:
        toys += 1
    i += 1

toys_total = toys * toy_price
money_saved_total = money_saved + toys_total

if money_saved_total >= washer_price:
    diff = float(money_saved_total - washer_price)
    print(f"Yes! {diff:.2f}")
else:
    diff = float(washer_price - money_saved_total)
    print(f"No! {diff:.2f}")