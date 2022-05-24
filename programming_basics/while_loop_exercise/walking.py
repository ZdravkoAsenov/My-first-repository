all_steeps = 0

while True:
    steep = input()

    if steep == "Going home":
        steep_home = int(input())
        all_steeps += steep_home
        if all_steeps >= 10000:
            diff = abs(all_steeps - 10000)
            print("Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
            break
        else:
            diff = abs(all_steeps - 10000)
            print(f"{diff} more steps to reach goal.")
            break

    all_steeps += int(steep)

    if all_steeps >= 10000:
        diff = abs(all_steeps - 10000)
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
        break
