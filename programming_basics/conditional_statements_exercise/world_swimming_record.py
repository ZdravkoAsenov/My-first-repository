from math import floor

record = float(input())
distance_meters = float(input())
time = float(input())

swimming_distance = distance_meters * time
delay = floor(distance_meters / 15) * 12.5
total_time = swimming_distance + delay

if record > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diff = abs(total_time - record)
    print(f"No, he failed! He was {diff:.2f} seconds slower.")