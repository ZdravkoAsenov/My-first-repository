price_trip = float(input())
count_puzzle = int(input())
count_talking_doll = int(input())
count_teddy_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

all_price = count_puzzle * 2.60 + count_talking_doll * 3 + count_teddy_bears * 4.10\
              + count_minions * 8.2 + count_trucks * 2
count_toys = count_trucks + count_minions + count_teddy_bears + count_talking_doll + count_puzzle

if count_toys >= 50:
    all_price = all_price - all_price * 0.25
rent = all_price - all_price * 0.9
total_prise = all_price - rent
if total_prise >= price_trip:
    print(f"Yes! {(total_prise - price_trip):.2f} lv left.")
else:
    print(f"Not enough money! {abs(total_prise - price_trip):.2f} lv needed.")