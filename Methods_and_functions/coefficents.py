def co(a,b,c):
    return (b**2-4*a*c)
d=(co(int(input("co-efficent of X^2 ")),int(input("co-efficent of X ")),int(input("constant "))))
if d>0:print("greter then zero")
elif d<0:print("less then zero")
elif d==0:print("equal to zero")
