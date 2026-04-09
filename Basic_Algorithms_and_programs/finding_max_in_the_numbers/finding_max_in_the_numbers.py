print("welcome to calculator")
a=int(input("please enter first number"))
b=int(input("enter the value of second number"))
c=int(input("enter the value of third number"))
if a>b and a>c:
            max=a
            if b<c:
               min=b
               print("maximum number is",max,"minimum number is",min)

            else:
                 min=c
                 print("maximum number is",max,"minimum number is",min)
elif b>a and b>c:
                max=b
                if a<c:
                  min=a
                  print("maximum number is",max,"minimum number is",min)
                else:
                     min=c
                     print("maximum number is",max,"minimum number is",min)
elif c>a and c>b:
                 max=c
                 if a<b:
                  min=a
                  print("maximum number is",max,"minimum number is",min)
                 else:
                     min=b
                     print("maximum number is",max,"minimum number is",min)
else:
               print("all are equal")
               
