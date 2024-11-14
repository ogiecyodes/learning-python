#TOTAL BILL TAX
# Write a python program that calculates the total bill after adding a sales tax of 7% to a given price
# Calculate the total bill for an item that costs N 175,050f
print ("Total Bill Tax")
item = input("Enter costumer item(s): ") # how do i enter multiple item
price =float(input(" Enter price of item:")) # how to input multiple price for each item
tax = ( 7 * price) / 100
total_bill = tax + price
print ("RECIEPT\n" "Price = " + str(price), "\n" "Sales Tax= " + str(tax) + "\n" + "Total Bill =" + str(total_bill))