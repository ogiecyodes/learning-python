from math import pi
def area_of_circle(radius)-> float:
  '''calculate the area of a circle '''
  return pi * (radius ** 2) 
value = area_of_circle(radius= float(input('Enter radius:')))
print(value)
  