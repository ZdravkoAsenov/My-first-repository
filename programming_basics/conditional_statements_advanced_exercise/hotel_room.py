mounth = input()
number_of_night = int(input())
apartment = 0
studio = 0

if mounth == "May" or mounth == "October":
    if number_of_night > 14:
        apartment = (65 - 65 * 0.1) * number_of_night
        studio = (50 - 50 * 0.3) * number_of_night
    elif number_of_night > 7:
        apartment = 65 * number_of_night
        studio = (50 - 50 * 0.05) * number_of_night
    else:
        apartment = 65 * number_of_night
        studio = 50 * number_of_night

if mounth == "June" or mounth == "September":
    if number_of_night > 14:
        apartment = (68.70 - 68.70 * 0.1) * number_of_night
        studio = (75.20 - 75.20 * 0.2) * number_of_night
    else:
        apartment = 68.70 * number_of_night
        studio = 75.20 * number_of_night

if mounth == "July" or mounth == "August":
    if number_of_night > 14:
        apartment = (77 - 77 * 0.1) * number_of_night
        studio = 76 * number_of_night
    else:
        apartment = 77 * number_of_night
        studio = 76 * number_of_night

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")