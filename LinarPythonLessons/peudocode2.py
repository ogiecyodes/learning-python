q = int(input("Input q: "))
r = int( input("Input r: "))
j = int( input("Input j: "))
q2 = q ** 2
root = r ** 0.5
num_bracket1 = q2 + root
denom_bracket1 = j ** 1/q
bracket1 = num_bracket1/denom_bracket1
num_bracket2 = 99 - q
denom_bracket2 = 49 ** 1/7
bracket_in = num_bracket2/denom_bracket2
bracket2 = bracket_in ** (20//6)
p = bracket1 / bracket2
print (p)