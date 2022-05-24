days = int(input())
type_room = input()
grade = input()
price = 0

if type_room == "room for one person":
    price = 18 * (days - 1)
    if grade == "positive":
        price += price * 0.25
    else:
        price -= price * 0.1

elif type_room == "apartment":
    price = 25 * (days - 1)
    if days < 10:
        price -= price * 0.30
    elif 10 < days < 15:
        price -= price * 0.35
    elif days > 15:
        price -= price * 0.50
    if grade == "positive":
        price += price * 0.25
    else:
        price -= price * 0.10

elif type_room == "president apartment":
    price = 35 * (days - 1)
    if days < 10:
        price -= price * 0.10
    elif 10 < days < 15:
        price -= price * 0.15
    elif days > 15:
        price -= price * 0.20
    if grade == "positive":
        price += price * 0.25
    else:
        price -= price * 0.1

print(f"{price:.2f}")