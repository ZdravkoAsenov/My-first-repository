balance = 0

while True:
    current_sum = input()
    if current_sum == "NoMoreMoney":
        print(f"Total: {balance:.2f}")
        break
    elif float(current_sum) < 0:
        print("Invalid operation!")
        print(f"Total: {balance:.2f}")
        break
    balance += float(current_sum)
    print(f"Increase: {float(current_sum):.2f}")