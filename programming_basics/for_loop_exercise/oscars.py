name_of_actor = input()
points_academy = float(input())
n = int(input())
give_points = 0

for i in range(n):
    name = input()
    points = float(input())
    give_points += (len(name) * points) / 2

    if points_academy + give_points >= 1250.5:
        break

total_points = points_academy + give_points

if total_points >= 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = abs(total_points - 1250.5)
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")