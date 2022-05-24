budget = int(input())
season = input()
number_of_fisher = int(input())
price_for_ship = 0

if season == "Spring":
    price_for_ship = 3000
    if number_of_fisher <= 6:
        price_for_ship -= price_for_ship * 0.1
    elif 7 < number_of_fisher <= 11:
        price_for_ship -= price_for_ship * 0.15
    elif number_of_fisher >= 12:
        price_for_ship -= price_for_ship * 0.25
    if number_of_fisher % 2 == 0:
        price_for_ship -= price_for_ship * 0.05

elif season == "Summer" or season == "Autumn":
    price_for_ship = 4200
    if number_of_fisher <= 6:
        price_for_ship -= price_for_ship * 0.1
    elif 7 < number_of_fisher <= 11:
        price_for_ship -= price_for_ship * 0.15
    elif number_of_fisher >= 12:
        price_for_ship -= price_for_ship * 0.25
    if season == "Summer" and number_of_fisher % 2 == 0:
        price_for_ship -= price_for_ship * 0.05

elif season == "Winter":
    price_for_ship = 2600
    if number_of_fisher <= 6:
        price_for_ship -= price_for_ship * 0.1
    elif 7 < number_of_fisher <= 11:
        price_for_ship -= price_for_ship * 0.15
    elif number_of_fisher >= 12:
        price_for_ship -= price_for_ship * 0.25
    if number_of_fisher % 2 == 0:
        price_for_ship -= price_for_ship * 0.05

diff = abs(budget - price_for_ship)

if budget >= price_for_ship:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")