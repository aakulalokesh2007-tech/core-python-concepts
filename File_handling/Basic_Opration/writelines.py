with open ("C:\\users\\monis\\Desktop\\test.txt",'w') as a:
   a.writelines(eval(input("group of values")))
print("finish")
with open ("C:\\users\\monis\\Desktop\\test.txt",'r') as a:
    b=(a.read())
print(b)
