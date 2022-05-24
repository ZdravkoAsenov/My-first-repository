import sys

n = int(input())
sum = 0
max_number = -sys.maxsize

for i in range(n):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    sum += current_number

if max_number == sum - max_number:
    print("Yes")
    print(f"Sum = {sum - max_number}")
else:
    sum = sum - max_number
    print("No")
    print(f"Diff = {abs(max_number - sum)}")
