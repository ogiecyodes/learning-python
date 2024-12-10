'''
def function (param1: param1datatype, param2:para2datatype)
args
param1 : param1datatype
param2 : param2datatype

return
return what it is programmed to return with specified datatype at the declaration line

print('function body')


'''
def deathyear_calculator(gender=str, year_of_birth =int) ->str:
  '''
  determine the year of death of the user based on gender and year of birth
  
  Args:
  year_of_birth = The year of birth of the user
  gender = The gender of the user (either "male" or "female")
  
  return the year on death based on the gender and average death age 
  
  '''
  if gender == "female":
    return year_of_birth + 104
  elif gender == "male":
    return year_of_birth + 96
  else:
    return "error"
user_data = deathyear_calculator(gender=(input("Enter gender: \n")), year_of_birth=int(input('Enter year of birth')))
print(user_data)
  
