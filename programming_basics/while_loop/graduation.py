name = input()
grade_counter = 0
bad_grade_counter = 0
average = 0.0

while grade_counter < 12:
    grade = float(input())

    if grade >= 4.00:
        grade_counter += 1
        average += grade
    else:
        bad_grade_counter += 1
        if bad_grade_counter > 1:
            print(f"{name} has been excluded at {grade_counter + 1} grade")
            break

if bad_grade_counter <= 1:
    print(f"{name} graduated. Average grade: {(average / grade_counter):.2f}")