#SIMPLE INTEREST CALCULATOR 
# Write a python program to calculate simple interest
print ("SIMPLE INTEREST CALCULATOR")
principal = float(input("please enter the Principal sum: "))
rate = float(input(" Please enter the interest rate applicable: "))
time= float(input('Please enter the duration (years): '))
calculation = (principal * rate * time) / 100
print(calculation)