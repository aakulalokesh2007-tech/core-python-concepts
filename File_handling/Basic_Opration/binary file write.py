from pickle import *
with open("hello.bat","wb") as a:
    for b in range(int(input("no of records"))):
        dump(input(str(b)+":"),a)
