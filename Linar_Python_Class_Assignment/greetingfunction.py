'''
def function (para1: para1datatype)
args
para1 : para1datatype
return
return what it is programmed to return based on the datatype
'''
def greet_user(name):
  '''
  determine a username  based on a user input, greet and welcome user after username input
  return 
  'hello' username, 'welcome'
  '''
  return f'hello {name}! welcome'
username = greet_user(name=(input("Enter username:")))
print(username)