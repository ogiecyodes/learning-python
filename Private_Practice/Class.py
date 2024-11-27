class BankAccount:
  #Construct a method to initialiaze account holder name and balance
  def __init__(property, accname, accbal=0):
    property.accname = accname #store the account holder's name in property
    property.accbal = accbal 
  def deposit(property, dep):
    property.accbal += dep
    print(f'depositing {dep}')
  def withdrawal(property, withdrawn):
    if property.accbal >= withdrawn:
      property.accbal -= withdrawn
      print(f'withdrawing {withdrawn}')
    else:
      print(f'insufficient balance')
  def getbalance(self):
    return self.accbal
  def __str__ (self):
    return f'Account Holder: {self.accname}, Balance: {self.accbal}'
  
object = BankAccount("Jaja opobo", 1000)
object.deposit(0)
object.withdrawal(300)
print(object)


  
    





