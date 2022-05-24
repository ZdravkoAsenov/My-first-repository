from math import floor

number_tournament = int(input())
starting_points = int(input())
tournament_points = 0
win_tournament = 0
for _ in range(number_tournament):
    position = input()

    if position == "W":
        tournament_points += 2000
        win_tournament += 1
    elif position == "F":
        tournament_points += 1200
    elif position == "SF":
        tournament_points += 720

total_points = starting_points + tournament_points
average_points = tournament_points / number_tournament
percent_win = (win_tournament / number_tournament) * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_win:.2f}%")
