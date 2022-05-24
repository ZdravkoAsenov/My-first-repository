first_number = int(input())
second_number = int(input())
magic_number = int(input())
combination = 0
flag = False

for i in range (first_number, second_number + 1):
    for n in range(first_number, second_number + 1):
        combination += 1
        result = i + n
        if result == magic_number:
            flag = True
            print(f"Combination N:{combination} ({i} + {n} = {magic_number})")
            break
    if flag:
        break

if not flag:
    print(f"{combination} combinations - neither equals {magic_number}")