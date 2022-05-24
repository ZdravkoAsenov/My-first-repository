from math import floor

lily_age = int(input())
price_for_washing_machine = float(input())
price_for_toy = int(input())
lily_money = 0
number_of_toy = 0

for i in range(1, lily_age + 1):
    if i % 2 == 0:
        lily_money += 10 * (i / 2)
    else:
        number_of_toy += 1

money_toy = number_of_toy * price_for_toy
brother_money = floor(lily_age/2)
total_money = money_toy + lily_money - brother_money

if total_money >= price_for_washing_machine:
    diff = total_money - price_for_washing_machine
    print(f"Yes! {diff:.2f}")
else:
    diff = abs(price_for_washing_machine - total_money)
    print(f"No! {diff:.2f}")