def starts_with_vowel(word)-> str:
  if word[0] == 'a'or word[0]=='e' or word[0] == 'i' or word[0] =='o' or word[0] =='u'or word[0] == 'A'or word[0]=='E' or word[0] == 'I' or word[0] =='O' or word[0] =='U':
    return f"{word} starts with vowel"
  else:
    return f"{word} does not start with vowel"
value = starts_with_vowel(word= input('Enter word to check if it starts with vowel:'))
print(value)
#vowels = 'aeiouAEIOU'
#return word[0] in vowels