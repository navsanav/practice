l=[]
while True:
    c=int(input("""
    1 push elements
    2 pop elements
    3 peak elements
    4 display elements
    5 exit
    """))

if c==1:
    n=input("enter the value")
    l.append(n)
    print(l)

if c==2:
    if len(l)==0:
        print("empty")
    else:
        p=l.pop()
        print(p)
        print(l)
if c==3:
    if len(l)==0:
       print("empty stack")
    else:
        print("last stack",l[-1])
if c==4:
    print("display stack",l)
elif c==5:
        break;