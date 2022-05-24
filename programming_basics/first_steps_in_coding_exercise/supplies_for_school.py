number_of_pen = int(input())
number_of_marker = int(input())
liter_of_detergent = int(input())
percentage_reduction = int(input())
total_price = number_of_pen * 5.80 + number_of_marker * 7.20 + liter_of_detergent * 1.20
final_prise = total_price - total_price * (percentage_reduction / 100)
print(final_prise)
