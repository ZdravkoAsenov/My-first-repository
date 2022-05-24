flag = False

while True:
    location = input()
    budget = float(input())
    sum = 0
    while location != "End":
        while sum < budget:
            current_money = input()
            sum += float(current_money)
            if sum >= budget:
                print(f"Going to {location}!" )
                sum = 0
                location = input()
                if location == "End":
                    flag = True
                    break
                budget = float(input())

    if flag:
        break
