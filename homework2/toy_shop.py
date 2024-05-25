puzzle = 2.60
doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2

field_trip = float(input())
number_of_puzzle = int(input())
number_of_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

ordered_toys = number_of_trucks+number_of_minions+number_of_teddy_bears+number_of_dolls+number_of_puzzle

total_price = float((puzzle * number_of_puzzle)+(doll * number_of_dolls)+(teddy_bear * number_of_teddy_bears)+(minion * number_of_minions)
+(truck * number_of_trucks))

if ordered_toys >= 50:
    total_price = total_price * 0.75

store_rent = total_price * 0.1

profit = total_price - store_rent

if profit >= field_trip:
    profit_after_paying_fieldtrip = profit - field_trip
    print(f"Yes! {profit_after_paying_fieldtrip} lv left.")
else:
    profit_after_paying_fieldtrip = field_trip - profit
    print(f"Not enough money! {profit_after_paying_fieldtrip} lv needed.")