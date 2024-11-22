def check_positive_negative(number=int):
  if number <0:
    return "Negative number" 
  else:
    return "Positive number"
value = check_positive_negative(number=int(input("Enter number:")))
print(value)
    
  
   