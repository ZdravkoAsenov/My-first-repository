budget = float(input())
number_love = int(input())
number_rose = int(input())
number_key = int(input())
number_karikature = int(input())
number_luky = int(input())

total_number = number_luky + number_karikature + number_key + number_rose + number_love

sum = (number_love * 0.60) + (number_rose * 7.2) + (number_key * 3.6) + (number_karikature * 18.2) + (number_luky * 22)

if total_number > 25:
    sum = sum - (sum * 0.35)

sum = sum - (sum * 0.1)

diff = abs(budget - sum)
if budget <= sum:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")