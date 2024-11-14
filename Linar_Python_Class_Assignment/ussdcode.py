#USSD code to check phone balance and buy airtime
print("LINAR USSD")
print("Please select an option:")
print("1. Check your Balance")
print("2. Buy Airtime")
print("3. Exit")
user_input = (input("Enter your choice (options 1-3): "))
if user_input == "1":
  print("Your Main account balance details has been sent to you as an SMS")
elif user_input == "2":
    airtime_amount = int(input("Enter the amount :"))
    pininput = (input('Enter 4 digit pin to recharge directly from your bank: '))
    pin = ["0000", "1111",  ] #create a list
    Bank_acc_bal = 1000
    if pininput == pin and  airtime_amount <= Bank_acc_bal:# Nested if statement
      print("Recharge successful!")
    elif pininput == pin and airtime_amount > Bank_acc_bal:
      print("Insufficient funds")    
    elif pininput != pin:
      print("Invalid Pin")
elif user_input == "3":
    print("Goodbye!")
else:
    print("Invalid selection. Please choose a valid option (1-3) ")
