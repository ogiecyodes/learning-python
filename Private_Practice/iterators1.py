numbers = [1,3,4,5,6,7,]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))

class learningitems:
  def __init__(self, items):
    self.items = items
    self.index = 0 #start at index, it can be 0, 1, 2...
  def __iter__(self):
    return self
  def __next__(self):
    if self.index >= len(self.items):
      raise StopIteration
    items = self.items[self.index]
    self.index += 1
    return items
  
items = ["apple", "berry", "mango", "orange", "cherry"]
iteemlist = learningitems(items)
for x in iteemlist:
    print(x)


    
    
  
   