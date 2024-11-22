#Tuple - ordered and unchangeable, allows duplicate item
# a comma must be used in a single tuple item for type to be identified as tuple
# Note that most things studied in list applies tuple
# Convert tuple to list to be able to change it
x = ("green", "white","green") # assigning value to a tuple is called packing a tuple
y = list(x)
y[2]= "grey"
x = tuple(y)
print (x)
a = ("mother", "father", "son")
b = list(a)
b.append("daughter") # we can also use the remove method
a = tuple(b)
print (a)
tuplelist = ("Catholics", "Muslims", "Christians")
add = ("Athiest",)
tuplelist += add
print (tuplelist)
#use of asterik in tuples
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
# Sets are undordered, unchangeable, and duplicates are not allowed
# True and 1, false and 0 are considered the same value in sets
setlist = {'oando', 'mobile', 'AP'}
setlist.add('totalenergies')
setlist.discard('oando')
setlist2 = {'Access', 'GTB', 'Zenith'}
ll = ('microfinance',)# note the comma for a single tuple object, 
setlist2.update(ll)
print (setlist2)
#union method
set1 = {'a', 'b', 'c'}
set2 = {'1', '2', '3'}
set3 = set1 | set2 # or set3 = set1.union(set2), note | operator only allows set to set joining, .union allow sets and other data collection
print (set3)
#intersection method - returns only objects that are duplicate in both sets. you can aslo use the & operator
set4 = {'c', 'd', 'e'}
set5 = {'p', 'e', 'a', 'c', 'e'}
set6 = set4.intersection(set5)
print (set6)
set4.intersection_update(set5)
print (set4)
#difference (-) method- returns item in the first set that are not present in the second set
set7 = {'c', 'd', 'e'}
set8 = {'p', 'e', 'a', 'c', 'e'}
set9 = set7.difference(set8)
print (set9)
set10 = set7 ^ set8 # symmentric difference - returns elements that do no appear in both sets
print (set10)
#isdisjoint method
set11 = set7.isdisjoint(set8) # it returns true if none of the items are present in both sets else it retuns false
print (set11)
#issubset <= and issuperset >= methods
set5 = {'p', 'e', 'a', 'c', 'e'}
set7 = {'c', 'd', 'e'}
set56 = set5.issubset(set7) #returns true if all item in set5 are present in set7 else returns false
print(set56)

#Dictionaries- ordered, changeable and do not allow duplicate
# key: value pairs
dict = {'brand': ' Toyota', 'Color': 'Grey', 'year': '2006', 'year':'2005', 'state': ['Abuja', 'Lagos']}
#dictconstructor = dict(name = 'peace', age = '20', gender = 'female')
#Acessing Dictionaries
newdict = {"Name": "Parker", 'Surname': 'Peter'}
x = newdict['Name']
print (x)
y = dict.get('year')
print (y)
z = dict.keys()
dict['model'] ='camry' # adding to a dictionary
print (z)
ze = dict.values()
print(ze)
ze = dict.items()
print (ze)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020}) #update method
thisdict = { # pop method deletes the specified item
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem() # removes the last inserted item
print(thisdict)
#loop in dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
# loop values
#for x in thisdict:
  #print(thisdict[x])
#for x in thisdict.values():
  #print(x)
# loop both keys and values
#for x, y in thisdict.items():
  #print(x, y)
#.copy() built in dictionary method
#Nested Dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#Or
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child2"]["name"])
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])
#fromkeys dictionary method
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y) # assigns values from y to key x 


print(thisdict)