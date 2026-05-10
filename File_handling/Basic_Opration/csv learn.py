from csv import*
with open("test.csv","w",newline="") as a:#new line default "\n"
     b=writer(a,delimiter=" ")
     b.writerow(["yes","its ","ok","byee"])
     b.writerow(["noo","byeee"])
    
with open("test.csv","r",newline="") as a:
    c=reader(a,delimiter=" ")#default ","
    print(tuple(c))
    