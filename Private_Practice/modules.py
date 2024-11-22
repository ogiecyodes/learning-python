import math
p = int(input("Enter any number:"))
squareRoot = math.sqrt(p)
print(squareRoot)
from math import factorial
x = 20
print(factorial(x))
import datetime as dt
y = dt.datetime.now().strftime("%Y-%m-%d,%H-%M-%S")
print(y)
import random as rd
random_numbers=[rd.randint(1,100) for i in range(10)] #creates a list of 10 random integers from 1-100
print(random_numbers)
maxnum = max(random_numbers)
minnum = min(random_numbers)
print(maxnum)
print(minnum)
import os
print(os.getcwd())
#os.mkdir(), os.chdir(), os.path.exists...
import sys
print(sys.version)



  
  