import sys

min_number = sys.maxsize
input_number = input()

while input_number != "Stop":
    if min_number > int(input_number):
        min_number = int(input_number)
    input_number = input()
print(min_number)