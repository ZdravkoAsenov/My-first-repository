jury = int(input())
average_grade = 0
grade_counter = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        print(f"Student's final assessment is {(average_grade / grade_counter):.2f}." )
        break
    grade = 0
    for i in range (1, jury + 1):
        current_grade = float(input())
        average_grade += current_grade
        grade_counter += 1
        grade += current_grade

    average = grade / jury
    print(f"{presentation_name} - {average:.2f}.")
    grade = 0




