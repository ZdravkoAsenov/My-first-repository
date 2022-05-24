hour_exam = int(input())
minute_exam = int(input())
hour_arrives = int(input())
minute_arrives = int(input())

time_exam = hour_exam * 60 + minute_exam
time_arrives = hour_arrives * 60 + minute_arrives

if time_exam == time_arrives:
    print("On time")
elif time_exam > time_arrives:
    if (time_exam - time_arrives) <= 30:
        print("On time")
        print(f"{time_exam - time_arrives} minutes before the start")
    elif (time_exam - time_arrives) < 60:
        print("Early")
        print(f"{time_exam - time_arrives} minutes before the start")
    else:
        print("Early")
        print(f"{(time_exam - time_arrives) // 60}:{((time_exam - time_arrives) % 60):02d} hours before the start")

elif time_exam < time_arrives:
    if (abs(time_exam - time_arrives)) < 60:
        print("Late")
        print(f"{abs(time_exam - time_arrives)} minutes after the start")
    else:
        print("Late")
        print(f"{abs(time_exam - time_arrives) // 60}:{(abs(time_exam - time_arrives) % 60):02d} hours after the start")