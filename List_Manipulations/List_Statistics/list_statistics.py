a=[];b=0
d=int(input("enter the number of element of list "))
for i in range(d):
    e=int(input("enter the element "))
    a.append(e)
print("your list is:")
print("         ",a)
print(''' to find max enter 1
to find min enter 2
to find sum enter 3''')
f=int(input("enter ch"))
if f==1:
    for g in a:
        if g>b:
            b=g
    print("the max no:",b)
elif f==2:
    b=a[0]
    for g in a:
       if g<b:
            b=g
    print("min:",b)
elif f==3:
    for g in a:
        b+=g
    print("the sum:",b)
    

      
