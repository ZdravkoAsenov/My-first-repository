money_need_for_journey = float(input())
available_money = float(input())
day_counter = 0
spend_counter = 0

while True:
    action = input()
    money = float(input())
    day_counter += 1

    if action == "spend":
        spend_counter += 1
        if money >= available_money:
            available_money = 0
        else:
            available_money -= money
        if spend_counter == 5:
            print("You can't save the money.")
            print(day_counter)
            break
    else:
        available_money += money
        spend_counter = 0
        if available_money >= money_need_for_journey:
            print(f"You saved the money for {day_counter} days.")
            break
