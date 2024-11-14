#write a program to calculate the average allowances of student in a month
# income received on a weekly basis.
# Make it user friendly by asking for name and department
# Ask name, department and month
username = input("Enter your username: ")
#We separate multiple words with underscore
user_dept = input("Enter your department: ")
print("welcome " + username.upper())
month = input ("what month are we calculating yur average allowance")
#method 1
wk1_allowance = input ("enter your week 1 allowance: ")
print (type(wk1_allowance))
convert_wk1_allowance =int(wk1_allowance)
print(type(convert_wk1_allowance))
#type function - complex type
x = 1j
print(type(x))

#method 2
wk_2_allowance = int(input("enter your week 2 allowance"))
wk_3_allowance = int(input("enter your week 3 allowance"))
wk_4_allowance = int(input("enter your week 4 allowance"))
Total_allowance = convert_wk1_allowance + wk_2_allowance + wk_3_allowance + wk_4_allowance
average_allowance =(Total_allowance/4)
print("Hello " + str(username) + " of " + str(user_dept) + " department. \n" "Thanks for using my calculator. \n"" your average allowance for the month of" + str(month)  + " is "
+ str(average_allowance))