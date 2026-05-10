#read a file:
##//////////////////// a file named "", will be opened with the reading mode.
file = open("C:\\users\\monis\\Desktop\\test.txt",'r')

#////////////# This will print every line one by one in the file
for each in file:
	print (each)
#second method:

# Python code to illustrate with()
with open("C:\\users\\monis\\Desktop\\test.txt") as file: 
	data = file.read() 

print(data)
