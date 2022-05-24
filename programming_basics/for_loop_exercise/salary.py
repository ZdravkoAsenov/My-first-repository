number_of_tabs = int(input())
salary = int(input())
conditional = False

for i in range(number_of_tabs):
    current_tab = input()

    if current_tab == "Facebook":
        salary -= 150
    elif current_tab == "Instagram":
        salary -= 100
    elif current_tab == "Reddit":
        salary -= 50

    if salary <= 0:
        conditional = True
        break

if conditional:
    print("You have lost your salary.")
else:
    print(salary)