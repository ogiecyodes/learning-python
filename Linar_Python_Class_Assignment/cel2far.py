def celsius_to_fahrenheit(celsius)->float:
  return (celsius * 9/5) + 32 
value = celsius_to_fahrenheit(celsius= float(input('Enter temperature in celsius:')))
print(value)