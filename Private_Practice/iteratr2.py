class myplayist:
  def __init__(self, numbers = 20):
    self.numbers = numbers
    self.index = 2
  def __iter__(self):
    return self
  def __next__(self):
    if self.index <= self.numbers:
      x = self.index
      self.index += 1
      return x
    else:
      raise StopIteration


for x in myplayist():
  print (x)
  
  
  