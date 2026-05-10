import csv
with open("csv.csv","r",newline="\n")as a:
    b=input("no of enters")
    for c in range(int(b)):
        d=input("::")
        csv.writer(a).writerow(d)

with open("csv.csv","r",newline="\n")as a:
    b=csv.reader(a,delimter=" ")
    for c in ((b)):
        print(c)
    
