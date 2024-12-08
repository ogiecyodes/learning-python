'''
def function (para1: para1datatype)
args
para1 : para1datatype
return
return what it is programmed to return based on the datatype
'''
from math import pi
def area_of_circle(radius=float)-> float:
  '''calculate the area of a circle '''
  return pi * (radius ** 2) 
value = area_of_circle(radius= float(input('Enter radius:')))
print(value)
  