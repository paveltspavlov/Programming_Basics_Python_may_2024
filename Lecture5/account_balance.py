deposit = input()

total = 0

while deposit != "NoMoreMoney":
    subtotal = float(deposit)
    if subtotal < 0:
        print("Invalid operation!")
        break

    print(f'Increase: {float(subtotal):.2f}')
    total += float(subtotal)
    deposit = input()

print(f"Total: {total:.2f}")
