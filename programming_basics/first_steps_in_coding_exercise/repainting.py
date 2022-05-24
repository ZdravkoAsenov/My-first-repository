nylon = int(input())
paint = int(input())
triner = int(input())
hour = int(input())
price_nylon = (nylon + 2) * 1.5
paint_price = (paint + (paint * 0.1)) * 14.5
triner_prise = triner * 5
materials_prise = price_nylon + paint_price + triner_prise + 0.40
work_price = (materials_prise * 0.3) * hour
print(materials_prise + work_price)