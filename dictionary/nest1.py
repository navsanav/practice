f={
    'a':{'name':'ashok kumar soni','age':'50','role':'father'},
    'b':{'name':"ratini devi soni",'age':'45','role':'mother'},
    'c':{'name':'sandeep soni','age':'25','role':'son'},
    'd':{'name':'pooja soni','age':'20','role':'sister'},
    'e':{'name':"hemlata soni",'age':'18','role':'choti behan'}
}

print(f['a']['name'])
print(f['b']['age'])

for k,b in f.items():
    print(k,b['name'],b['role'])
