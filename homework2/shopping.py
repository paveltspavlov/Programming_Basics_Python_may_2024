budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

video_cards_price = 250
processors_price = float(video_cards_price * 0.35)
ram_price = float(video_cards_price * 0.10)

final_video_cards_price = float(video_cards_price * video_cards)
final_processors_price = float((final_video_cards_price * 0.35) * processors)
final_ram_price = float((final_video_cards_price * 0.10) * ram)

total_price = float(final_ram_price + final_processors_price + final_video_cards_price)

if video_cards > processors:
    total_price = total_price * 0.85

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
