def count_uppercase(text):
  return sum(1 for x in text if x.isupper())# signifies the number or step it adds or increases as it counts the uppercases
#isupper()method used to check for upper cases in a string
value = count_uppercase(text= input('Enter any word with upper and lower cases:'))
print(value)