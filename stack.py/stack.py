l=[]
while True:
    c=int(input('''
    1 Push Elements
    2 Pop Elements
    3 Peek Elements
    4 Display stack
    5 Exit
    
    '''))

    if c==1:
        n=input("enter the value")
        l.append(n)
        print(l)
    if c==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            p=l.pop()
            print(p)
            print(l)
    if c==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("peek elements",l[-1])
    if c==4:
        print("display stack",l)
    elif c==5:
        break;

