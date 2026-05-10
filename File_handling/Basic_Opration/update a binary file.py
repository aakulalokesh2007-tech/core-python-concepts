from pickle import *
with open ("hello.bat","rb+") as a:
    try:
        while True:
            c=a.tell()
            b=load(a)
            
                
            print(b)
    except EOFError:
        print("\nthe end")
            
        
