number_people = int(input())
number_point = float(input())
season = input()
place = input()
sum = 0

if place == "Bulgaria":
    sum = number_point * number_people
elif place == "Abroad":
    sum = (number_point * number_people) * 1.5

if place == "Bulgaria":
    if season == "summer":
        sum = sum - (sum * 0.05)
    elif season == "winter":
        sum = sum - (sum * 0.08)
if place == "Abroad":
    if season == "summer":
        sum = sum - (sum * 0.1)
    elif season == "winter":
        sum = sum - (sum * 0.15)

money_for_charitable = sum * 0.75

money_for_people = sum - money_for_charitable

print(f"Charity - {money_for_charitable:.2f}")
print(f"Money per dancer - {(money_for_people / number_people):.2f}")
