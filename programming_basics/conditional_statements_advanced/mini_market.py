type_of_product = input()
town = input()
quantity = float(input())
price = 0

if town == "Sofia":
    if type_of_product == "coffee":
        price = 0.50
    elif type_of_product == "water":
        price = 0.80
    elif type_of_product == "beer":
        price = 1.20
    elif type_of_product == "sweets":
        price = 1.45
    elif type_of_product == "peanuts":
        price = 1.60
elif town == "Plovdiv":
    if type_of_product == "coffee":
        price = 0.40
    elif type_of_product == "water":
        price = 0.70
    elif type_of_product == "beer":
        price = 1.15
    elif type_of_product == "sweets":
        price = 1.30
    elif type_of_product == "peanuts":
        price = 1.50
elif town == "Varna":
    if type_of_product == "coffee":
        price = 0.45
    elif type_of_product == "water":
        price = 0.70
    elif type_of_product == "beer":
        price = 1.10
    elif type_of_product == "sweets":
        price = 1.35
    elif type_of_product == "peanuts":
        price = 1.55

total_price = price * quantity

if total_price > 0:
    print(total_price)