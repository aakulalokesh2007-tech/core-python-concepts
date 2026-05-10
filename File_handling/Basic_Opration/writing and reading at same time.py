# r+ and w+ both r same
a= open("C:\\Users\\monis\\Desktop\\test.txt",'r+')
a.write("hello friendsa")
a.close()
a= open("C:\\Users\\monis\\Desktop\\test.txt",'r+')
b=a.read()
print(b)
a.close()
