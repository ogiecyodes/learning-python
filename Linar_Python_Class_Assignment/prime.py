def is_prime(number=int)->int:
  """Check if a number is prime."""
  return number % 2 != 0
value = is_prime(number= int(input('Enter number:')))
print(value)