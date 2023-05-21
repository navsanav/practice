d=[]
while True:
    c=int(input("""
    1 push elemnets
    2 pop elements
    3 peek elements
    4 display stack
    5 exit
    """))

    if c==1:
        n=input("enter the value")
        d.append(n)
        print(d)
    if c==2:
        if len(d)==0:
            print("empty stack")
        else:
            p=d.pop()
            print(p)
            print(d)
    if c==3:
        if len(d)==0:
            print("empty stack")
        else:
            print("peak elements",d[-1])
    if c==4:
        print("display stack",d)
    if c==5:
        break; 
