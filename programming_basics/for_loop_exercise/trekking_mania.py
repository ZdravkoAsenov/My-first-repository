number_group = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
total_people = 0

for i in range(number_group):
    number_people = int(input())
    total_people += number_people

    if number_people <= 5:
        p1 += number_people
    elif 6 <= number_people <= 12:
        p2 += number_people
    elif 13 <= number_people <= 25:
        p3 += number_people
    elif 26 <= number_people <= 40:
        p4 += number_people
    elif number_people >= 41:
        p5 += number_people

print(f"{p1 / total_people * 100:.2f}%")
print(f"{p2 / total_people * 100:.2f}%")
print(f"{p3 / total_people * 100:.2f}%")
print(f"{p4 / total_people * 100:.2f}%")
print(f"{p5 / total_people * 100:.2f}%")
