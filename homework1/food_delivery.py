chicken = float(10.35)
fish = float(12.40)
vegetarian = float(8.15)
deilivery_fee = float(2.50)

chicken_meals_count = int(input())
fish_meals_count = int(input())
vegetarian_meals_count = int(input())

total_price_main_course = float((chicken * chicken_meals_count) + (fish_meals_count*fish) + (vegetarian_meals_count*vegetarian))

desert = float(total_price_main_course * 0.2)

total_price = float(total_price_main_course + desert + deilivery_fee)

print(total_price)
