import math

n = int(input())
m = float(input())
total_km = 0

for i in range (1, n+1):
    percent = int(input())
    total_km += m
    m = m + (m * (percent / 100))

total_km += m

diff = abs(1000 - total_km)
if total_km >= 1000:
    print(f"You've done a great job running {math.ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(diff)} more kilometers")