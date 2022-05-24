import sys

max_number = -sys.maxsize
input_number = input()

while input_number != "Stop":
    if max_number < int(input_number):
        max_number = int(input_number)
    input_number = input()
print(max_number)