a=[]
while True:
    b=int(input("""
    1 Push elemnets
    2 Pop  elements
    3 Peek elements
    4 display stack
    5 exit
    
  """))
    if b==1:
        n=input("Push elements")
        a.append(n)
        print(a)
    if b==2:
        if len(a)==0:
            print("empty stack")
        else:
            c=a.pop()
            print(c)
            print(a)
    if b==3:        
       if len(a)==0:
            print("Empty Stack")
       else:
           print("Peak Elements",a[-1])
    if b==4:
          print("display stack",a)
    if b==5:
        break;
            

