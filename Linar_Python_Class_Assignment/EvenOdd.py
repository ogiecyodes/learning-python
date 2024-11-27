def is_even(number):
  """Check if a number is even."""
  return number % 2 == 0
value = is_even(number= int(input('Enter number:')))
print(value)