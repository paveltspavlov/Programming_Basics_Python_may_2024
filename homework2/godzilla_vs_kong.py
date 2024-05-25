budget = float(input())
actors = int(input())
clothes_price_for_one_actor = float(input())

decor_price = budget * 0.1

if actors > 150:
    clothes_price_for_one_actor = clothes_price_for_one_actor * 0.9

if  decor_price + actors * clothes_price_for_one_actor <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - (decor_price + actors * clothes_price_for_one_actor):.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {(decor_price + actors * clothes_price_for_one_actor) - budget:.2f} leva more.")