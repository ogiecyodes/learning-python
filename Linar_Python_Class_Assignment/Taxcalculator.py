print("Welcome to Apex Tax Calculator \n" "We help with accurate tax computation of your monthly salary \n"
      "Please kindly answer the questions below ")
Name = input ("What is your name?: ")
company = input ("Name of Company?: ")
Month = input ("Which salary month do you want your tax computed?: ")
income = float(input("What is your salary for the month of " + str(Month) + "?: " ))
expenses = float(input ("What is your total expenses for the month of " + str(Month)+ "?: " ))
Balance = income - expenses
#using the f-string to combine string with float/integers
b = f"Balance of Salary after expenses is: {Balance:.2f}"
print(b)
Tax = (3)*(Balance)/100
print("Your tax payable for the month of " + str(Month) + " is " + str(Tax))
print("Thank you " + str(Name) + " for using Apex Tax Calculator!")