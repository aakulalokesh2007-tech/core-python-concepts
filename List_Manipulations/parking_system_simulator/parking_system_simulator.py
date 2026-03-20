
print(''' information:
                cartype can be of three kinds :big,medium,or small which are represented by 1,2,3 respectively''')


h=[]
k=[]
while True:
    b=input("number of big sized cars can be parked ")
    if b.isdigit():
        b=int(b)
        break
    else:
        print("wrong value!.please enter a number  ")
while True:
    c=input("number of middium sized cars can be parked ")
    if c.isdigit():
        c=int(c)
        break
    else:
         print("wrong value!.please enter a number ")
while True:
    d=input("number of small sized cars can be parked ")
    if d.isdigit():
        d=int(d)
        break
    else:
        print("wrong value!.please enter a number ")
a=[b,c,d]
total_cars=sum(a)
while True:
    e=input(f"number of cars are there enter less than {total_cars} ")
    if e.isdigit() and int(e)<=total_cars:
        e=int(e)
        break
    else:
        print(f"wrong value!.please enter a number less {total_cars}")
for f in range (e):
    while True:
        g=input("enter the code of the car type '1'[big];'2'[medium];'3'[small] ")
        if g.isdigit():
            g=int(g)
            if g not in (1,2,3):
                print("wrong code!.plz enter a valid code")
                continue
            else:
                break
        else:
            print("wrong value!.please enter a number")
    i=[g]
    h.append(i)
h.insert(0,a)
print("Input is :")
print("       ",h)
h.remove(a)
for j in h:
    if j[0]==1:
        if a[0]>0:
            a[0]-=1
            k.append(True)
        else:
            k.append(False)
    elif j[0]==2:
        if a[1]>0:
            a[1]-=1
            k.append(True)
        else:
            k.append(False)
    elif j[0]==3:
        if a[2]>0:
            a[2]-=1
            k.append(True)
        else:
            k.append(False)
k.insert(0,'null')
print("The output is :")
print("         ",k)
        
        
