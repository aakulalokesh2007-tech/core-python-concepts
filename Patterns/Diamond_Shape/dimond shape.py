while True:
    b=input("enter the number of lines or press enter to stop")
    if b=="":
        break
    if b.isdigit():
       b=int(b)
       if b%2!=0:
        for a in range(1,b,2):
            print(" "*(b-a) ,"* "*(a))
        for c in range (b,0,-2):
            print(" "*(b-c),"* "*(c))
   
       elif b%2==0:
           for a in range(0,b,2):
               print(" "*(b-a),"* "*(a+1))
           for c in range(b,0,-2):
               print(" "*(b-(c-1))," *"*(c-1))
       
         
input()
