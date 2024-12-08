G = open('Highcourtcasefile.txt' , 'r')#"r" is used to read a txt file
print(G.read())
print(G.read(5))
print(G.readline())
#for x in G:
  #print(x)
G.close()#close the file

