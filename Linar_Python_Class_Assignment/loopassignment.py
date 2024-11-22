# Ecommerce site that loops through selected  List items and adds them to cart
items = ['LV Sneakers','Mouka foam', 'HP Laptop' ,'Iphone 16']
for x in items:
    print (f" added to cart : {x}")
    
# Job application that that allows you apply if you within the age range 
birthyear = int(input("Enter Birth year: "))
if birthyear < 1997:
  print (f"{birthyear} not within qualified age range for application")
elif birthyear >= 1997 and birthyear <=2004:
    print(f"{birthyear} is qualified" )
else:
  print ("underage")
import datetime
now = datetime.datetime.now()
age= int(input('year of birth'))
currrent_age= now.year - age
if currrent_age >27 or currrent_age <18 : 
  print(f"{currrent_age} yrs old not qualified. Job age range must be 18-27")
else:
  print(f'{currrent_age}qualified')
  