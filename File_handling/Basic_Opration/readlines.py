with open("test.txt") as file:
        data1=[a.strip()for a in file.readlines()]
        #for a.strip() in file.readlines():
                #data1+=[a]
        file.seek(0)
        print( file.readlines()) 
print(data1[1][-1])
