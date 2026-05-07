d = {'country': 'Germany',
     'capital': 'Berlin'}
f = open('file.txt', 'w')
f.write(str(d))
f.close()
f = open('file.txt', 'r')
data = (f.read())
print(data)
f.close()
