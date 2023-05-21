a=[]
while True:
    c=int(input("""
    1 push elements
    2 pop elements
    3 peek elements
    4 display stack
    5 exit
    """))
    if c==1:
        n=input("enter the value")
        a.append(n)
        print(a)
    if c==2:
        if len(a)==0:
          print("empty stack")
        else:
           l=a.pop()
           print(l)
           print(a)
    if c==3:
       if len(a)==0:
           print("empty stack")
       else:
           print("peek elements",a[-1])
    if c==4:
        print("display stack",a)
    if c==5:
        break; 
