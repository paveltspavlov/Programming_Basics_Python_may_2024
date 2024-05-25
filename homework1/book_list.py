number_of_pages = int(input())
pages_per_hour = int(input())
days = int(input())

days_to_finish_the_book = number_of_pages / pages_per_hour
hours_per_day_needed_to_finish_book = days_to_finish_the_book/days

print(int(hours_per_day_needed_to_finish_book))
