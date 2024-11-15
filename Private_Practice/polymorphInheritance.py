class vehicle:
  pass
  def fuel_efficiency(self):
    pass
class truck (vehicle):
  def __init__(self, loadweight, fuelcom, dist ):
    self.loadweight = loadweight
    self.fuelcom = fuelcom
    self.dist = dist
  def fuel_efficiency(self):
    return (self.dist/self.fuelcom) * self.loadweight
class motorcycle(vehicle):
  def __init__(self, fuelcom, dist ):
    self.fuelcom = fuelcom
    self.dist = dist
  def fuel_efficiency(self):
    return (self.dist/self.fuelcom) 
class car(vehicle):
  def __init__(self,fuelcom, dist ):
    self.fuelcom = fuelcom
    self.dist = dist
  def fuel_efficiency(self):
    return (self.dist/self.fuelcom) 
  
object = [truck(20,50,100), motorcycle(20,50), car(5, 44) ]
for x in object:
  print(x.fuel_efficiency())
    