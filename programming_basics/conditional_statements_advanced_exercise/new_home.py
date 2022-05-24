type_of_florals = input()
number_of_florals = int(input())
budget = int(input())
price_for_florals = 0

if type_of_florals == "Roses":
    price_for_florals = number_of_florals * 5
    if number_of_florals > 80:
        price_for_florals -= price_for_florals * 0.1
elif type_of_florals == "Dahlias":
    price_for_florals = number_of_florals * 3.8
    if number_of_florals > 90:
        price_for_florals -= price_for_florals * 0.15
elif type_of_florals == "Tulips":
    price_for_florals = number_of_florals * 2.8
    if number_of_florals > 80:
        price_for_florals -= price_for_florals * 0.15
elif type_of_florals == "Narcissus":
    price_for_florals = number_of_florals * 3
    if number_of_florals < 120:
        price_for_florals += price_for_florals * 0.15
elif type_of_florals == "Gladiolus":
    price_for_florals = number_of_florals * 2.5
    if number_of_florals < 80:
        price_for_florals += price_for_florals * 0.20

diff = abs(budget - price_for_florals)

if budget >= price_for_florals:
    print(f"Hey, you have a great garden with {number_of_florals} {type_of_florals} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")