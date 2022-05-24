budget = float(input())
number_video_card = int(input())
number_processor = int(input())
number_ram = int(input())

price_video_card = number_video_card * 250
price_processor = (price_video_card * 0.35) * number_processor
price_ram = (price_video_card * 0.10) * number_ram
total_price = price_ram + price_processor + price_video_card

if number_video_card > number_processor:
    total_price = total_price - (total_price * 0.15)

if total_price <= budget:
    diff = budget - total_price
    print(f"You have {diff:.2f} leva left!")
else:
    diff = abs(budget - total_price)
    print(f"Not enough money! You need {diff:.2f} leva more!")