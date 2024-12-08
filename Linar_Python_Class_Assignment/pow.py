'''
def function (para1: para1datatype, para2: paradatatype)
args
para1 : para1datatype
para2: para2datatype
return
return what it is programmed to return based on the datatype
'''
from math import pow
def calculate_power(base, exponent = int)->int:
  ''' Calculate the power of a number'''
  return pow(base, exponent)
value = calculate_power(base= int(input('Enter base number:')), exponent=int(input("Enter exponent number ")))
print(value)