name_airport = input()
number_tickets_for_adults = int(input())
number_tickets_for_kids = int(input())
price_for_adults = float(input())
tax = float(input())

kids_ticket = price_for_adults * 0.30

total_price = ((price_for_adults + tax) * number_tickets_for_adults) + ((kids_ticket + tax) * number_tickets_for_kids)
money = total_price * 0.20

print(f"The profit of your agency from {name_airport} tickets is {money:.2f} lv.")

