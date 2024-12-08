def remove_vowels(word):
  vowels ='aeiouAEIOU'
  consonant = ''
  for x in word:
    if x not in vowels:
      consonant += x
  return consonant
value = remove_vowels(word= input('Enter word:'))
print(value)