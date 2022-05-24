price_of_luggage_over_20_kg = float(input())
pounds_of_luggage = float(input())
days_before_the_trip = int(input())
number_of_luggage = int(input())
price = 0

if pounds_of_luggage < 10:
    price = price_of_luggage_over_20_kg * 0.20
elif 10 <= pounds_of_luggage <= 20:
    price = price_of_luggage_over_20_kg * 0.50
elif pounds_of_luggage > 20:
    price = price_of_luggage_over_20_kg

if days_before_the_trip > 30:
    price += price * 0.10
elif 7 <= days_before_the_trip <= 30:
    price += price * 0.15
elif days_before_the_trip < 7:
    price += price * 0.40

total_price = price * number_of_luggage

print(f"The total price of bags is: {total_price:.2f} lv. ")
