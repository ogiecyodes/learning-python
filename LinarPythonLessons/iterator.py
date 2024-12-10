class tryagain:
  def __init__(self, numbermax = 20):
    self.a = 0
    self.numbermax = numbermax
  def __iter__(self):
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 2
      return x
    else:
      raise StopIteration
    
for x in tryagain():
  print(x)
    