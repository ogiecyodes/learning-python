
L = int(input("INPUT L: "))
F = int(input("INPUT F: "))
S = int(input("INPUT s: "))
W = int(input("INPUT w: "))
n = int(input("INPUT n: "))
RSE = F ** n
RSB = (S * L)/F
RSSB = (20/F)** W
Denominator = 20 ** n/3
bracket_sum = RSB + RSSB
numerator = RSE * bracket_sum
finalanswer = numerator/ Denominator
Y = finalanswer
print (Y)
