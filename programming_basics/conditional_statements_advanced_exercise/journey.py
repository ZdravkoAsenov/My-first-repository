budget = float(input())
season = input()
price_for_journey = 0

if budget <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        price_for_journey = budget * 0.30
        print(f"Camp - {price_for_journey:.2f}")
    else:
        price_for_journey = budget * 0.70
        print(f"Hotel - {price_for_journey:.2f}")
elif budget <= 1000:
    print("Somewhere in Balkans")
    if season == "summer":
        price_for_journey = budget * 0.40
        print(f"Camp - {price_for_journey:.2f}")
    else:
        price_for_journey = budget * 0.80
        print(f"Hotel - {price_for_journey:.2f}")
elif budget < 10000:
    print("Somewhere in Europe")
    price_for_journey = budget * 0.90
    if season == "summer":
        print(f"Hotel - {price_for_journey:.2f}")
    else:
        print(f"Hotel - {price_for_journey:.2f}")