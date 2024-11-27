class Dog:
  def __init__ (self):
    pass
  def makesound(self):
    print("Bark! is for Dog")
    
class Cat:
  def  __init__(self):
    pass
  def makesound(self):
    print ("meow is for Cat")

objectD = Dog()
objectC = Cat()
for x in (objectC, objectD):
  x.makesound()
  

    