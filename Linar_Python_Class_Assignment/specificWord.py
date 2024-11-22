def specificWord(Sentence, word):
  if word in Sentence:
    return True
  else:
    return False
value = specificWord(Sentence=("I Love Python"),word=('Python'))
print(value)