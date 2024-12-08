'''
def function (para1: para1datatype)
args
para1 : para1datatype
return
return what it is programmed to return based on the datatype
'''
def is_palindrome(word = str)->bool:
  """Check if a word is a palindrome."""
  return word == word[::-1]
value = is_palindrome(word= input('Enter word:'))
print(value)
  