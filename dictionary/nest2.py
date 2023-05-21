b={
    'deepika':{'age':'25','colour':'gori','figure':'34-30-34','type':'maal'},
    'isha':{'age':'24','colour':'gori-mam','figure':'30-32-34','type':'atom bomb'},
     'xyz':{'age':'unknown','colour':'pata ni','figure':'null','type':'xyz'},
    
}

print(b['isha']['colour'])

for k,l in b.items():
    print(k,l['colour'],l['figure'])