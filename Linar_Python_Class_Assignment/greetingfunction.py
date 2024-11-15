'''
def function (para1: para1datatype)
args
para1 : para1datatype
return
return what it is programmed to return based on the datatype

'''
def greet_user(name):

  '''
  determine a username  based on a user input
  return the greeting 'hello' withe the username inputed
  
  
  '''
  return f'hello {name}! welcome'
username = greet_user(name=(input("Enter username:")))
print(username)

