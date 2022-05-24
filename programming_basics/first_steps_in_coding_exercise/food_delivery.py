chiken_menu = int(input())
fish_menu = int(input())
vegitarian_menu = int(input())
menu_price = chiken_menu * 10.35 + fish_menu * 12.40 + vegitarian_menu * 8.15
dessert_price = menu_price * 0.2
total_price = menu_price + dessert_price + 2.5
print(round(total_price, 2))