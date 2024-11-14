#Comparison Operators and Logical Operators
age = int(input("age: "))
gender = input("gender: ")
if age >= 18 and gender == "female":
  print(age >= 18 and gender == "female")
  print ("Access granted")
else:
  print("Access denied")
yearlysalary =int(30000 * 12)
ys = f"{yearlysalary:.2f}"
print (ys)
root_of_9 = 9 ** (0.5)
print(root_of_9)
print (9 >=9)
#AND logical operator
x = 30
print (x > 20 and x < 10)
Nigeria = "West_Africa"
print (Nigeria != "North_Africa" and Nigeria != "East_Africa")
fruits = "pine" + "apple"
print( fruits == "pineapple" and fruits != "apple")
x = 1995
if x > 2005:
  print (x)
#OR logical operator
dice_roll = int(input("Enter Dice Roll: "))
if dice_roll ==  3 or dice_roll == 5:
  print ("You rolled the dice to ODD!") 
  print ("You've 1 point ")



