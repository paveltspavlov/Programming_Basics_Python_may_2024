resto = float(input())
buff_money = 0.0
number_of_coins = 0

while resto > 0.01:
    if resto >= 2:
        resto -= 2
        buff_money += 2
        number_of_coins += 1
    elif resto >= 1:
        resto -= 1
        buff_money += 1
        number_of_coins += 1
    elif resto >= 0.5:
        resto -= 0.5
        buff_money += 0.5
        number_of_coins += 1
    elif resto >= 0.2:
        resto -= 0.2
        buff_money += 0.2
        number_of_coins += 1
    elif resto >= 0.1:
        resto -= 0.1
        buff_money += 0.1
        number_of_coins += 1
    elif resto >= 0.05:
        resto -= 0.05
        buff_money += 0.05
        number_of_coins += 1
    elif resto >= 0.02:
        resto -= 0.02
        buff_money += 0.02
        number_of_coins += 1
    elif resto >= 0.01:
        resto -= 0.01
        buff_money += 0.01
        number_of_coins += 1
    else:
        break

if resto < 0.01:
    number_of_coins += 1
    print(number_of_coins)
else:
    print(number_of_coins)
