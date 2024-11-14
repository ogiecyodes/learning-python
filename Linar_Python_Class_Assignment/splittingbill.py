# Write a program to split the restaurant bill between a group of friends
bill = float(input( "input bill "))
people = int(input("number of people "))
tip = float(input( "tip percentage "))
tip_bill = (tip * bill ) /100
split= (tip_bill + bill) / people
print ("Each person is to pay ", split)