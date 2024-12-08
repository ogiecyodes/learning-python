'''
def function (para1: para1datatype)
args
para1 : para1datatype
return
return what it is programmed to return based on the datatype
'''
def check_positive_negative(number=int)-> int:
  ''' Enter an integer and return if the integer is a positive or negative number'''
  if number <0:
    return "Negative number" 
  else:
    return "Positive number"
value = check_positive_negative(number=int(input("Enter number:")))
print(value)
    
  
   