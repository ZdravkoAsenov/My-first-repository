sum_prime = 0
sum_non_prime = 0
flag = False

while True:
    current_number = input()

    if current_number == "stop":
        break
    number = int(current_number)
    if int(number) < 0:
        print("Number is negative.")
    else:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    flag = True
                    break
            if flag:
                sum_non_prime += number
            else:
                sum_prime += number
            flag = False
            
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")