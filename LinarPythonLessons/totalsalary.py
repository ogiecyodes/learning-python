# Write a program to calculate the total salary of an employee with base salary of $2000, 10% bonus and 12% tax
print("Congratulation on your job offer!!!\n Fill the details below to get your total salary (net)")
base_salary = float(input("Enter Base Salary: "))
bonus = float(input("Enter Bonus percentage (%): "))
tax_rate = float(input("Enter tax rate applicable : "))
base_bonus = (bonus * base_salary)/100
tax = (tax_rate * base_salary)/100
total_salary = base_salary + base_bonus - tax 
print("SALARY BREAKDOWN\n" "base_salary = " + str(base_salary),"\n" + "Bonus = "+ str(base_bonus) + "\n" "Tax deductible = " + str(tax), "\n" "Toal Salary (Net) =" + str(total_salary))