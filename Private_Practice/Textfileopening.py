#p = open('Highcourtcasefile.txt', 'x')# 'x' used to create a txt file
#p.close()


p = open ('Highcourtcasefile.txt', 'a')
p.write("\n2.The Claimant is suing the Defendant for negligence")

p = open('Highcourtcasefile.txt' , 'r')#"r" is used to read a txt file
print(p.read()) 

import os 
os.remove('demo.txt')# used to remove a file
if os.path.exists('demo.txt'):# used to check if file exists
  os.remove('demo.txt')
else:
  print('file dosent exist')
os.rmdir('my folder')# used to remove folder, only empty folders
