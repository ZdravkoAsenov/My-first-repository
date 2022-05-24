number_people = int(input())
number_nights = int(input())
number_card = int(input())
number_ticket = int(input())

price = ((number_nights * 20) + (number_card * 1.6) + (number_ticket * 6)) * number_people
total_price = price + (price * 0.25)

print(f"{total_price:.2f}")
