goal_for_day = int(input())
sum = 0

while True:
    type = input()
    if type == "closed":
        break
    if type == "haircut":
        operation = input()
        if operation == "mens":
            sum += 15
        elif operation == "ladies":
            sum += 20
        elif operation == "kids":
            sum += 10

    elif type == "color":
        operation = input()
        if operation == "touch up":
            sum += 20
        elif operation == "full color":
            sum += 30

    if sum >= goal_for_day:
        break


if sum >= goal_for_day:
    print(f"You have reached your target for the day!")
else:
    diff = abs(sum - goal_for_day)
    print(f"Target not reached! You need {diff}lv. more.")

print(f"Earned money: {sum}lv.")