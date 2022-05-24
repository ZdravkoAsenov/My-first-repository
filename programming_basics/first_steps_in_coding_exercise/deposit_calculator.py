deposit_price = float(input())
deposit_term = int(input())
annual_interest = float(input())
interest = deposit_price * (annual_interest / 100)
interest_for_month = interest / 12
total_sum = deposit_price + deposit_term * interest_for_month
print(total_sum)