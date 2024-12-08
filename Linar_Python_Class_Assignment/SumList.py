'''
def function (para1: para1datatype)
args
para1 : para1datatype
return
return what it is programmed to return based on the datatype
'''
def sum_list(numberlist=int)->int:
  ''' determine the sum of a list of numbers and return the summed value'''
  return sum(numberlist)
value = sum_list(numberlist=[1,2,4,6,8])
print(value)