def simpleInterest(p,r,t=float)->float:
  return p * r * t / 100
calculation = simpleInterest(p=float(input('principal ')),r=float(input('rate ')),t=float(input('time ')))
print(calculation)


