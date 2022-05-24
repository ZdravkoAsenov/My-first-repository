number_joinery = int(input())
type_of_joinery = input()
delivery = input()
total_price = 0

if number_joinery < 10:
    print("Invalid order")
else:
    if type_of_joinery == "90X130":
        if number_joinery > 60:
            total_price = (number_joinery * 110) * 0.92
        elif number_joinery > 30:
            total_price = (number_joinery * 110) * 0.95
        else:
            total_price = (number_joinery * 110)
    elif type_of_joinery == "100X150":
        if number_joinery > 80:
            total_price = (number_joinery * 140) * 0.90
        elif number_joinery > 40:
            total_price = (number_joinery * 140) * 0.94
        else:
            total_price = (number_joinery * 140)
    elif type_of_joinery == "130X180":
        if number_joinery > 50:
            total_price = (number_joinery * 190) * 0.88
        elif number_joinery > 20:
            total_price = (number_joinery * 190) * 0.93
        else:
            total_price = (number_joinery * 190)
    elif type_of_joinery == "200X300":
        if number_joinery > 50:
            total_price = (number_joinery * 250) * 0.86
        elif number_joinery > 25:
            total_price = (number_joinery * 250) * 0.91
        else:
            total_price = (number_joinery * 250)

    if delivery == "With delivery":
        total_price += 60

    if number_joinery > 99:
        total_price *= 0.96

    print(f"{total_price:.2f} BGN")