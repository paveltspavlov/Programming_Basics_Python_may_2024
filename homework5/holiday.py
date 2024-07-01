money_needed = float(input())
money_available = float(input())
days = 0
spend_counter = 0

while money_available < money_needed and spend_counter < 5:

    activity = input()
    amount = float(input())
    days += 1

    if activity == "save":
        money_available += amount
        spend_counter = 0
    elif activity == "spend":
        money_available -= amount
        spend_counter += 1
        if money_available < 0:
            money_available = 0

    if spend_counter == 5:
        print(f"You can\'t save the money.")
        print(days)

    if money_available >= money_needed:
        print(f"You saved the money for {days} days.")
