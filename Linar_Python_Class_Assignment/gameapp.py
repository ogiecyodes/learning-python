#Gameapp
print (' Welcome to Game Crush \t Select an Option below')
options = input(" 1.Play \n 2. Select Level \n 3.Exit \n ")
if options == "1":
  player = input("Enter Gameusername: ")
  print ("Welcome to Game Crush" + str(player))
  GameCharacter= input ("Choose Game Character \n 1. ENOCH \n 2. JOY \n 3. SAMSON ")
  print ('Loading...')
elif options == "2":
  levels = input("select level \n Easy \n Hard \n Difficult \n")
elif options == "3":
  exit = input ("Are you sure you want to exit \n a. YES \n b. NO")
  if exit == "a": print ("goodbye") 
  else:print ("Continue Game")
  
  
  