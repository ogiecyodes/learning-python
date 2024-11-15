class Dog:
  def __init__ (self):
    pass
  def makesound(self):
    print("Bark!")
    
class Cat:
  def  __init__(self):
    pass
  def makesound(self):
    print ("meow")

objectD = Dog()
objectC = Cat()
for x in (objectC, objectD):
  x.makesound()
  

    