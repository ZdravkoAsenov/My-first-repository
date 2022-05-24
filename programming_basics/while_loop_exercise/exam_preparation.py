number_bad_grade = int(input())
bad_grade_counter = 0
conditional = False
grade_counter = 0
average_grade = 0
last_example = ''


while True:
    name_example = input()

    if name_example == "Enough":
        average = average_grade / grade_counter
        print(f"Average score: {average:.2f}")
        print(f"Number of problems: {grade_counter}")
        print(f"Last problem: {last_example}")
        break
    grade_example = int(input())

    if grade_example <= 4:
        bad_grade_counter += 1
        if bad_grade_counter == number_bad_grade:
            print(f"You need a break, {bad_grade_counter} poor grades.")
            break

    average_grade += grade_example
    grade_counter += 1
    last_example = name_example

