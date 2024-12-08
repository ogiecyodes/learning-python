import re
def is_valid_email(email=str)->bool:
  emailpattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+.[a-zA-Z0-9._-]+$'
  ''' r used to return a raw string, ^indicates the start of a string
  [a-zA-Z0-9_-+]to match when any of these charaters, @ to match when the @ symbol
  $- indicates the end of a string. 
  Checks if the entire email string matches the specified regex pattern.
  returns a bool- True or False
  '''
  return bool (re.match(emailpattern, email))
value = is_valid_email(email=(input('Enter email address:')))
print(value)