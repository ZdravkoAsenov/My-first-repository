time_first = int(input())
time_second = int(input())
time_third = int(input())
sum_second = time_first + time_second + time_third

if sum_second < 60:
    minute = sum_second // 60
    second = sum_second
    if second < 10:
        print(f"{minute}:0{second}")
    else:
        print(f"{sum_second // 60}:{sum_second}")

elif sum_second >= 60 and sum_second < 120:
    minute = sum_second // 60
    second = sum_second - 60
    if second < 10:
        print(f"{minute}:0{second}")
    else:
        print(f"{sum_second // 60}:{second}")

elif sum_second >= 120:
    minute = sum_second // 60
    second = sum_second - 120
    if second < 10:
        print(f"{minute}:0{second}")
    else:
        print(f"{sum_second // 60}:{second}")