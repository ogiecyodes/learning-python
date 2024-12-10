import re
txt = 'I love python'
r = re.findall('[a-p]', txt)
a = re.search('python', txt)# the search function returns a match object
b = re.split('love',txt)
c = re.sub('I', "u", txt)
print(r)
print(a.start())
print(a)
print(b)
print(c)
