import json
#parse a json string to dictionary using json.loads
x = '{"Name": "John", "Age": "30"}'
y = json.loads(x)
print(y['Age'])
a  = {
  "Name": "John", 
  "Age": 30,
  "city": "Port Harcourth",
  "Children": None,
  "Status": "Single"
  }
b = json.dumps(a, indent=2, sort_keys=True)# converts to json string
print(b)

print(json.dumps(("apple", "banana", "mango"))) #tuple to list

