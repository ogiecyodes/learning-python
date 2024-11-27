def is_palindrome(word):
  """Check if a word is a palindrome."""
  return word == word[::-1]
value = is_palindrome(word= input('Enter word:'))
print(value)
  