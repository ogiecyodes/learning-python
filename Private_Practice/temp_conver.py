#Temperature Conversion from celsius to fahrenheit
c2f = 'celsius to fahrenheit temperature conversion calculator'
print(c2f.upper())
celsius = float(input("Enter your temperature: \n"+ "\t"+ "\b" +"\b" +"'\b"+ "\b" +chr(176) +"C\r"))
conversion = (celsius * 9/5) + 32 
fahrenheit = conversion
print (str(celsius)+chr(176) +"C", "=" ,str(fahrenheit)+chr(176) +"F")
print ("Your temperature in fahrenheit is " + str(fahrenheit) +chr(176) +"F")





