import json

# simple example
data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"] + "\n")
print("###########################################\n")

# complex example
data1 = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info1 = json.loads(data1)
print('User count:', len(info1))

for item in info1:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])