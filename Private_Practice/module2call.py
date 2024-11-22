import modules2
name = input("what is your name? ")
print(modules2.greet_user(name))
numbers = (input("enter numbers sperated by spaces"))
number = [int(x) for x in numbers.split()]#coverting the inputed str to a list of integers
print(number)
print(modules2.find_average_number(number))