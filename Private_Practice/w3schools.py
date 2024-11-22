#Multiple variables
x, y, z = "May", "June", "March"
print(x, y, z)
x = y= z = "love"
print(x)
print(y)
print(z)
x = "James "
y = "Peter "
z = "Andrew"
print (x + y + z)
x = "fantastic"
def myfunc():
  global x
  x = 'awesome'
myfunc()
print(" i am " + x)
# Data type - tuple
x = ("apples", "bananas", "goat")
print(type(x))
#frozenset
xy = frozenset({"apple", "banana","cherry"})
print(type(xy))
#Dict 
y = {"name" : "abeeb", "age": 36}
print(type(y))
# Set
p ={"apple", "grapes", "mango"}
print(type(p))
#bytes
q = b"Hello"
print (type(q))
#random
import random
print(random.randrange(2,9))
#Strings are arrays of bytes-learn string slicing
jo = "Daniel"
print(jo[5])
print (jo[-5])
print (jo[2:]) 
print(jo[2:5])
print(jo[-3:-1])
print(len(jo))
price = 59
sample = f"\bThe price is {price:.1f} pounds"
print(sample)
#List - ordered and changeable-allows duplicate item
List=["go", "no", "is", 56,]
print(List[3])
print(len(List))
time = list(("12pm", "3pm", "8pm"))
time[2] = "6pm"
time.insert(0, "10am")
time.append("8pm")
time.extend(List)
time.remove("12pm")
time.pop()#removes last item if no index is specified
del time[4]
time.clear()
print(time)
Months = ["January", "December", "March"]
a, b, c = Months
print (a)
if "December" in Months:
  print("It's \"christmas\" season")
else:
  print("False")
#loop List
Alphabeths =["a", "g", "n", "e", "s"]
for k in Alphabeths:
  print(k)
#List comprehension
oldlist = ["covenant", "Babcock", "Bayero"]
newlist = [ x for x in oldlist if "e" in x ] #for is return in my interpretation
print(newlist)
r = [ x for x in range(6) if x != 2]
print (r)
newlist = [ x.upper() for x in oldlist ]
print(newlist)
newlist = [" how" for x in oldlist]
print (newlist)
Animals = ["lion", 'goat', "pig" ] 
Animals.sort()
print(Animals)
Numbers = [90, 56, 34, 20, 7]
Numbers.sort()
print(Numbers)
Numbers.sort(reverse=True)
print(Numbers)
# Note also that sort function is case sensitive and would print case in caplock in first order
Animals = ["Lion", 'goat', "Pig" ] 
Animals.sort()
print(Animals)
Animals = ["lion", 'goat', "pig" ] 
Animals.sort(key= str.lower)
print(Animals)
def myfunc(p): # yet to understand this
  return abs(p // 90)
Numbers = [90, 56, 34, 20, 7, 100]
Numbers.sort(key = myfunc)
print(Numbers)
Animals = ["lion", 'goat', "pig" ] 
Animals.reverse()
print(Animals)
new = Animals.copy() # or Animal[:] this is called the slice operator used as a copy function
print (new)
# joining List
List_1 = [1,2,3, 6, 6]
List_2 = [4,5,6]
q = List_1.count(6) # returns the number of time a value appears in a list
print (q)
List_2.extend(List_1)
print (List_2)
for x in List_1:
  List_1.append(List_2)
print(List_1)