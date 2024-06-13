lily_age = int(input())
washer_price = float(input())
toy_price = int(input())

money_saved = 0
money_saved1 = 0
toys = 0
money_taken = 1
i = 0
buff = 0
buff2 = 0

for i in range(i, lily_age):

    if i % 2 == 0:
        buff += 10
#        money_saved += buff
        money_saved += buff
        money_taken += buff2
        print(money_saved)
        print(money_taken)
        print("__________")
        buff2 =+ 1
    else:
        toys += 1

    i += 1

toys_total = toys * toy_price
money_saved_total = money_saved + toys_total - money_taken

if money_saved_total >= washer_price:
    diff = float(money_saved_total - washer_price)
    print(f"Yes! {diff:.2f}")
else:
    diff = float(washer_price - money_saved_total)
    print(f"No! {diff:.2f}")
