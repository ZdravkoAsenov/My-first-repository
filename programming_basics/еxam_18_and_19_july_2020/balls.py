from math import floor

number = int(input())
points = 0
red_ball = 0
orange_ball = 0
yellow_ball = 0
white_ball = 0
black_ball = 0
other_ball = 0

for i in range(1, number + 1):
    current_ball = input()
    if current_ball == "red":
        points += 5
        red_ball += 1
    elif current_ball == "orange":
        points += 10
        orange_ball += 1
    elif current_ball == "yellow":
        points += 15
        yellow_ball += 1
    elif current_ball == "white":
        points += 20
        white_ball += 1
    elif current_ball == "black":
        points = floor(points / 2)
        black_ball += 1
    else:
        other_ball += 1

print(f"Total points: {points}")
print(f"Red balls: {red_ball}")
print(f"Orange balls: {orange_ball}")
print(f"Yellow balls: {yellow_ball}")
print(f"White balls: {white_ball}")
print(f"Other colors picked: {other_ball}")
print(f"Divides from black balls: {black_ball}")

