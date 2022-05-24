type_of_product = input()
day_of_week = input()
quantity = float(input())
price = 0
if day_of_week in "Monday Tuesday Wednesday Thursday Friday ":
    if type_of_product == "banana":
        price = 2.50
    elif type_of_product == "apple":
        price = 1.20
    elif type_of_product == "orange":
        price = 0.85
    elif type_of_product == "grapefruit":
        price = 1.45
    elif type_of_product == "kiwi":
        price = 2.70
    elif type_of_product == "pineapple":
        price = 5.50
    elif type_of_product == "grapes":
        price = 3.85
    else:
        print("error")

elif day_of_week in "Saturday Sunday":
    if type_of_product == "banana":
        price = 2.70
    elif type_of_product == "apple":
        price = 1.25
    elif type_of_product == "orange":
        price = 0.90
    elif type_of_product == "grapefruit":
        price = 1.60
    elif type_of_product == "kiwi":
        price = 3.00
    elif type_of_product == "pineapple":
        price = 5.60
    elif type_of_product == "grapes":
        price = 4.20
    else:
        print("error")
else:
    print("error")

total_sum = price * quantity

if total_sum > 0:
    print(f"{total_sum:.2f}")