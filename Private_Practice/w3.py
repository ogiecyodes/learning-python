def cumulativescore(*a): # not defining the number of arg to call
  cumulative =  a[1] 
  print(cumulative)
cumulativescore(50, 60,45,30,10)

def cumulativescore(n): 
  return lambda a : a * n
additin  = cumulativescore(4) 
print(additin(10)) # mulitples cumulativescore with  number passed as result, 

x = lambda a,b,c : a + b +c
print (x(2,2,2))
  





