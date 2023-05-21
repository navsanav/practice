a={
    'name':'sandeep soni',
   'age':'25'
   }
b=a.get('name')
print(b)

for k in a.keys():
    print(k)

for k in a.values():
    print(k)

for k,l in a.items():
    print(k,l)
del a['age']
print(a)

print(a.pop('name'))

b=dict(name="sandeep soni",lover="bubly urf bulbul")
print(b) 