money = int(float(input()) * 100)
coins = 0

while money > 0:
    if money >= 200:
        money -= 200
        coins += 1
    elif money >= 100:
        money -= 100
        coins += 1
    elif money >= 50:
        money -= 50
        coins += 1
    elif money >= 20:
        money -= 20
        coins += 1
    elif money >= 10:
        money -= 10
        coins += 1
    elif money >= 5:
        money -= 5
        coins += 1
    elif money >= 2:
        money -= 2
        coins += 1
    elif money >= 1:
        money -= 1
        coins += 1

print(coins)