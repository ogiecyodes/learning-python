class shape:
  def __init__(self, color):
    self.color = color
  def describe(self):
    return f"This shape is {self.color}."
class circle(shape):
  def __init__(self, color, radius):
    super().__init__(color)
    self.radius = radius
  def area(self):
    return 3.14 * (self.radius ** 2)
  def describe(self):
    super().describe()
    print(f"This circle is {self.color} with a radius of {self.radius}.") 
class rectangle(shape):
  def __init__(self, color, width, height):
    super().__init__(color)
    self.width =width
    self.height = height
  def area(self):
    return self.width * self.height
  def describe(self):
    super().describe()
    print(f"This rectangle is {self.color} with a width of {self.width} and a height of {self.height}")
object = circle("red",20)
object.describe()
print("Area", object.area())
object = rectangle("blue", 12 ,18)
object.describe()
print("Area", object.area())
    
  
