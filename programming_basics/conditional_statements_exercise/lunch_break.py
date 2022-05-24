import math

name_serial = input()
time_episode = int(input())
time_break = int(input())

time_lunch = time_break * 0.125
time_rest = time_break * 0.25

time_left = time_break - (time_lunch + time_rest)

if time_episode <= time_left:
    diff_enough = time_left - time_episode
    print(f"You have enough time to watch {name_serial} and left with {math.ceil(diff_enough)} minutes free time.")
else:
    diff_not_enough = abs(time_left - time_episode)
    print(f"You don't have enough time to watch {name_serial}, you need {math.ceil(diff_not_enough)} more minutes.")