class shape:
  def area(self):
    pass
class circle(shape):
  def __init__(self, radius):
    self.radius = radius
  def area(self):
    return 3.14 * (self.radius ** 2)
class rectangle(shape):
  def __init__(self, areaR):
    self.areaR = areaR
  def area(self):
    return self.areaR * self.areaR
  
objects = [circle(20), rectangle(10)]
for x in objects:
  print(x.area())
    
    