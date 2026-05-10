#writeing a file:

a=open("C:\\users\\monis\\Desktop\\test.txt",'w')
st=input("enter")
b=a.write(st)
print(b)
a.close()

' ' ' '# second method
with open ("C:\\users\\monis\\Desktop\\test.txt",'w') as a:
    a.write(input("str"))
    a.write(input("2str"))
