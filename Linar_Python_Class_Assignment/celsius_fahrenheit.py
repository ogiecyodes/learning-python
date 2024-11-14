#Write a program asking the user whether he or she wants to convert celsius to fahrenheit or fahrenheit to celsius
print('Temperature conversion calculator') 
ask = input(" choose the option \"a\" or \"b\" \n a) celsius to fahrenheit \n b) fahrenheit to celsius \n : ")# use the backlash to enable a quote in a quote
if ask == "a": # if condition must end with a colon 
  c2f = float(input("Enter your temperature (Celsius):")) # if condition works with identation
  conversion = (c2f * 9/5) + 32 
  fahrenheit = conversion
  print (str(c2f)+chr(176) +"C", "=" ,str(fahrenheit)+chr(176) +"F")#chr()function is used to generate strings, symbols etc that have an equivalent unicode which is an integer number ex. 176 is the unicode that is equivalent to degree symbol
elif ask == "b":
  f2c = float(input("Enter your temperature (Fahrenheit):"))
  conversion2 = (f2c - 32) * 5/9 # take note of operator precedence to avoid logical error
  celsius = conversion2
  print (str(f2c)+chr(176) +"F", "=" ,str(celsius)+chr(176) +"C")
else:
  print("invalid option")