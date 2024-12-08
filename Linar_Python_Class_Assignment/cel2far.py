'''
def function (para1: para1datatype)
args
para1 : para1datatype
return
return what it is programmed to return based on the datatype
'''
def celsius_to_fahrenheit(celsius = float)->float:
  ''' convert tempearture in celsius to fahreheit '''
  return (celsius * 9/5) + 32 
value = celsius_to_fahrenheit(celsius= float(input('Enter temperature in celsius:')))
print(value)