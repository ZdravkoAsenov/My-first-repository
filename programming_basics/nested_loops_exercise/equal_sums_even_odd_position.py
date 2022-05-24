first_number = int(input())
second_number = int(input())

for i in range (first_number, second_number + 1):
    even_sum = 0
    odd_sum = 0

    for n in range(len(str(i))):

        if n % 2 == 0:
            even_sum += int(str(i)[n])
        elif n % 2 != 0:
            odd_sum += int(str(i)[n])
    if even_sum == odd_sum:
        print(i, end=" ")