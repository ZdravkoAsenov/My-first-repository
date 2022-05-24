student = 0
standard = 0
kid = 0
total = 0
name = input()

while True:
    current_student = 0
    current_standard = 0
    current_kid = 0
    current_total = 0
    if name == 'Finish':
        break
    free_seats = int(input())
    while True:
        seat = input()

        if seat == 'End':
            print(f'{name} - {current_total / free_seats * 100:.2f}% full.')
            break

        current_total += 1
        total += 1

        if seat == 'student':
            student += 1
            current_student += 1
        elif seat == 'standard':
            standard += 1
            current_standard += 1
        elif seat == 'kid':
            kid += 1
            current_kid += 1

        if current_total >= free_seats:
            print(f'{name} - {current_total / free_seats * 100:.2f}% full.')
            break

    name = input()

print(f'Total tickets: {total}')
print(f'{student / total * 100:.2f}% student tickets.')
print(f'{standard / total * 100:.2f}% standard tickets.')
print(f'{kid / total * 100:.2f}% kids tickets.')