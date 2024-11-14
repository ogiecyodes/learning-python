#Write a program t calculate the body mass weight of a user
print ("BMI CALCULATOR")
weight = float(input("please enter weight (kg): "))
height = float(input(" Please enter height (m): "))
bmical = weight/(height**2)
print ("BMI =" , bmical)