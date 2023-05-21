d={
    'a':{'name':'sandeep soni','age':'25','married':'no'},
    'b':{'name':'himanshu sharma','age':'24','married':'no'},
    'c':{'name':'rahul sharma','age':'24','married':'no'}
}
#print(d)
#for k,b in d.items():
    #print(k,b)

#print(d['a']['name'])

for k,b in d.items():
    print(k,b['name'],b['age'])
    