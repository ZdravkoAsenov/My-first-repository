budget_movie = float(input())
count_statists = int(input())
price_clothes = float(input())


price_decor = budget_movie * 0.1
total_price_clothes = count_statists * price_clothes
total_price_for_movie = price_decor + total_price_clothes

if count_statists > 150:
    discoint = total_price_clothes - (total_price_clothes * 0.1)
    total_price_for_movie = discoint + price_decor

if budget_movie >= total_price_for_movie:
    print("Action!")
    print(f"Wingard starts filming with {abs(budget_movie - total_price_for_movie):.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget_movie - total_price_for_movie):.2f} leva more.")