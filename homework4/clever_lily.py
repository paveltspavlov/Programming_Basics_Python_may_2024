lily_age = int(input())
washer_price = float(input())
toy_price = int(input())

money_saved = 0
toys = 1
money_taken = 0
i = 0
buff = 0

while i < lily_age:

    if i % 2 == 0:
        buff += 1
        money_saved += buff*10
        money_taken += 1

    else:
        toys += 1

    i += 1


toys_total = toys * toy_price
print(money_taken)
print(money_saved)
money_saved_total = (money_saved + toys_total) - money_taken
print(money_saved_total)

if money_saved_total >= washer_price:
    diff = float(money_saved_total - washer_price)
    print(f"Yes! {diff:.2f}")
else:
    diff = float(washer_price - money_saved_total)
    print(f"No! {diff:.2f}")
