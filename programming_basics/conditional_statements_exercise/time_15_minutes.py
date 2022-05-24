input_hour = int(input())
input_minute = int(input())
total_minute = (input_hour * 60) + input_minute + 15
hour = total_minute // 60
minute = total_minute % 60
if hour > 23:
    print(f"0:{minute:02d}")
else:
    print(f"{hour}:{minute:02d}")