import functools
l=[1,2,3,4,5]
fu=lambda x,y:x+y
a=functools.reduce(fu,l)
print(a)
