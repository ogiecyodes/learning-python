"""FINAL EVALUATION
PYTHON PROGRAMMING LANGUAGE
DURATION: 1:45 MINS
Instructions: Answers 7 questions, Number 1, 5 and 9 is compulsory, Pick any 4 others. 
Remember, this evaluation has a lot to do with your certification.

"""

"""
You are advised not to cheat in any for, its an advice and not a must, since it’s not a must you get certified too.  
1)	Variable Data Types 
a) Create a variable called "Date_Of_Birth" and assign it the year you were born (or any random year) using the right datatype. Print the value of the variable. 
b) What is the difference between an integer and a floating-point number in Python? Backup your explanation with an example for each.
c) Explain the types of Logical operators with scenerios.

# QUestion 1 answer goes in here:
"""
Date_of_Birth = "1990" #The datatype could be a string
Date_of_Birth = 1990 #The datatype could be an integer

"""
1b) An Integer is repreents whole number data type while a floating-point represents number data type with decimal points. An example of an Integer is 10,
an example of a floating-point number is 4.5 
1c) There are three types of logical operators:
AND, OR, NOT 
AND operator returns True if both the conditions are met, OR operator returns True if either of the conditions,
NOT operator returns True if the condition is False and False if the condition is True.
x = 30
print (x > 20 and x < 40) This will return True because both conditions are True. i.e x which is 30 is greater than 20 and less than 40
print (x > 20 or x < 10) This will return True because either of the condition is True. x which is 30 is greater than 20, this is the only True condition
print (not(x> 20)) This will return False because the condition is not met. 


2)	Basic Operations 
a) Write a Python program that adds two numbers together and prints the result. 
b) Write a Python program that takes a number as input and multiplies it by 10. Print the result.



# QUestion 2 answer goes in here:

"""

x = 5
y= 10
p = sum([x,y])
print(p)

#or 
print(x + y)

x = int(input('Enter number:'))
print(x * 10)
"""
3)	Control Structures 
a) Write a Python program that checks if a number is even or odd. If the number is even, print "Even", otherwise print "Odd". 
b) Write a Python program that takes a number as input and checks if it is positive, negative, or zero. Print the result.




# QUestion 3 answer goes in here:

"""
def is_even_or_is_odd(number):
  if number % 2 == 0:
    return 'Even number'
  elif number % 2 !=0:
    return "Odd number"
value = is_even_or_is_odd(number= int(input('Enter number:')))
print(value)


def check_positive_negative_or_zero_number(number=int)-> int:
  if number <0:
    return "Negative number" 
  elif number == 0:
    return "Zero"
  else:
    return "Positive number"
value = check_positive_negative_or_zero_number(number=int(input("Enter number:")))
print(value)

"""
4)	Lists, Loops and Data Structure
a) Create a list of numbers from 1 to 10. Print each number in the list using a loop. 
b) Write a Python program that takes a list of numbers as input and returns the sum of all the numbers in the list.
c) Create a dictionary ‘colleague_name’ storing all your colleague names. Hint: Use sequence of numbers as their key.  





# QUestion 4 answer goes in here:

"""
numbers_list =[1,2,3,4,5,6,7,8,9,10]
for x in numbers_list:
  print(x)
  
def sum_list(a):
  return sum(a)
value = sum_list(a=[1,2,3,4,5])
print(value)

colleague_name = {
  1: 'Joy',
  2: 'Enoch',
  3: 'Dami',
  4: 'Samson'
}

"""
5)	Functions 
a) Write a Python function that takes three numbers as input and return their multiplication. 
b) Write a Python function that takes a list of numbers as input and returns the average of all the numbers in the list.
c) Greet a User: Write a function greet_user(name) that takes a person's name as input and returns a greeting message.
Example: Output: "Hello, Alice! Welcome!"
d) Calculate Simple Interest: Write a function simple_interest(principal, rate, time) that calculates simple interest.
Example: Input: simple_interest(1000, 5, 2)
Output: 100.0

e) Convert Minutes to Seconds: Write a function minutes_to_seconds(minutes) that converts a given number of minutes into seconds.
Example:
Input: minutes_to_seconds(5)
Output: 300





# QUestion 5 answer goes in here:

"""
def three_numbers(a,b,c)->int:

  return (a * b * c)
value = three_numbers(a=int(input('Enter number')), b=int(input('Enter number')), c=int(input('Enter number:')))
print(value)

def average_number(numberlist=int)->int:
  return sum(numberlist)/len(numbers_list)
value = average_number(numberlist=[1,2,4,6,8])
print(value)

def greet_user(name):
  return f'Hello {name}! welcome'
username = greet_user(name=(input("Enter username:")))
print(username)

def simple_interest(p,r,t=float)->float:
  return p * r * t / 100
calculation = simple_interest(p=float(input('principal ')),r=float(input('rate ')),t=float(input('time ')))
print(calculation)

def minute_to_seconds(minutes=int)->str:
  seconds = minutes * 60
  return f'{seconds} seconds '
cal = minute_to_seconds(minutes=(int(input("Enter Minutes: "))))
print (cal)

"""
6)	Libraries and Modules 
a) Install and Import the "math" module and use its "sqrt" function to calculate the square root of a number. 
b) Install and Import the "random" module and use its "randint" function to generate a random number between 1 and 10.
c) Install and Import the "pywhatkit" module and use its "whatsapp" function to send a DM to your tutor with the body “Good Day Sir”



# QUestion 6 answer goes in here:

"""
from math import sqrt
x = int(input('Enter number:'))
print(sqrt(x))


from random import randint
print(randint(1,10))


"""
7)	 Explain the following terms relating to Python programming Language with examples where needed
a)	Escape Sequence
b)	Keywords
c)	Datatypes
d)	Dictionary 
e)	Module
f)	Interpreter
g)	Give a brief history of python, who built it, what led to Python and others, state the current version of python you are using.




# QUestion 7 answer goes in here:

"""


"""
8)	Mentions some tools used the career listed below, write extensively on the career you are choosing after this course. Explain what the career entails and the problem skilled professionals in the career solve in the real-world market.
a)	Data Scientist
b)	Software Engineer
c)	Data Engineer
d)	Data Analytics
e)	Web Developer (Backend Developer)
f)	Machine Learning Engineer




# QUestion 8 answer goes in here:


"""



"""
9)	Give a feedback on this Python course, your instructor and this examination.


Question 9 answer goes in here:
My Feedback on Python 

Python is a very understandable programming language to learn. it is not complex and complicated.
The instructor is knowledgable and pushes for his student to be the very best and to also go beyond what has been taught,he does this
by giving loads of tasks and assignments to stretch our capabilities as pythonistas
The examination is good and not far-fetched from our prior tasks and assignment, i am happy i did them, even though i cant remember all, it made the exam 80% easy




BEST OF LUCK
"""