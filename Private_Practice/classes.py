class student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade
    
  def greeting(self,):
    print ('Hello my name ' + self.name +'I am ' + str(self.age) )
    
  def passed(self):
    if self.grade >= 50:
      print("you passed")
    else:
      print("you failed")
    
    
object = student("Jaja", 16, 46)
object.greeting()
object.grade = 66 #modify object properties
object.passed()
  

    