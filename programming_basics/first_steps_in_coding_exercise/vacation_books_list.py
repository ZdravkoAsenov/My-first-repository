number_of_pages = int(input())
pages_for_hour = int(input())
number_of_days = int(input())
total_hour_for_book = number_of_pages // pages_for_hour
required_hour = total_hour_for_book // number_of_days
print(required_hour)