p = open('Highcourtcasefile.txt', 'x')# 'x' used to create a txt file
p = open('Highcourtcasefile.txt', 'a')# append to the txt file
p.write('1. The Claimant is a company duly registered under the laws of Nigeria')
p.close()
p = open('Highcourtcasefile.txt', 'r')
print(p.read())