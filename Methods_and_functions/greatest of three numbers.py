def great(a,b,c):
    d=sorted([a,b,c])
    return d[-1]
a,b,c=eval(input("enter three numbers n1,n2,n3 "))
print(great(a,b,c))
