# Ecommerce site that loops through selected  List items and adds them to cart
items = ['LV Sneakers','Mouka foam', 'HP Laptop' ,'Iphone 16']
for x in items:
    print (f" added to cart : {x}")
    
# Job application that that allows you apply if you within the age range 
birthyear = int(input("Enter Birth year: "))
yearlist = (1997, 1998, 1999, 2000,2001, 2002,2003, 2000)
for x in yearlist: 
  if yearlist > 1997: print (f"{birthyear} not within qualified age range for application")
  elif yearlist < 1996 and yearlist >2000:
    print(f"{birthyear} is qua" )