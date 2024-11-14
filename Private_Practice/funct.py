#def function_name (argument, argument2, argument3):
  #statement1
  #statement1
  #return "value"

def normal_addition (a,b):
  total = int(a) + int(b)
  print (total)
normal_addition (10, 20)
normal_addition (20, 30)

def asking_gender():
  user_gender = input('kindly input your gender by choosing just M or F ')
  if user_gender.upper() == 'M':
    return "Sir" 
  elif user_gender.upper() == 'F':
    return "Ma"
  else:
    return "happily"
  
def name_department(name, department):
  gender_salutation = asking_gender()
  statement = (f'You are welcome {name} The {department} department welcomes you {gender_salutation} to Linar')
  return statement

print(name_department("Joy", " Python"))

def myfunction(*, name):#if you do not know how many key word to be passed use **
  print("my name is " , name['fname'] )
myfunction(fname = 'Peace', mname = 'Imuentiyanosa', lname = 'Ogie')#keywords arguments, key = value, kwargs

def africancountry(country = 'Nigeria'):
  print(" i love", country)
africancountry() # default parameter value passed as Nigeria
africancountry('Ghana')
africancountry('South Africa')
africancountry ('Rwanda')

def listfunction(fruits):
  for x in fruits:
    print (x)
fruits = ['banana', 'apple', 'pineapple']
listfunction(fruits)  
  
def positionalarg(p,/):
  print (p)
positionalarg(10)