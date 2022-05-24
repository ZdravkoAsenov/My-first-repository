first_border = int(input())
second_border = int(input())
third_border = int(input())

for first in range (1, first_border + 1):
    for second in range(1, second_border + 1):
        for third in range(1, third_border + 1):
            if first % 2 == 0 and third % 2 == 0:
                if second == 3 or second  == 5 or second == 7 or second == 2:
                    print(f"{first} {second} {third}")