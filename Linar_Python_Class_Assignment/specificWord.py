def specificWord(Sentence, word):
  if word in Sentence:
    return True
  else:
    return False
value = specificWord(Sentence=input("Enter any sentence:"),word= input('Enter word to check if in sentence:'))
print(value)