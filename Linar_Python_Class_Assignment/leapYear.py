
import datetime 
def is_leap_year(year):
  try:
    datetime.datetime(year, 2, 29)
    return "leap year"
  except ValueError:# exception handling, handles the value-error that would have been raised with if-else statement
    return f" {year} not a leap year"
value = is_leap_year(year= int(input('Enter year:')))
print(value)