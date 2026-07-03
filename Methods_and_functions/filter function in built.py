a=[("a","F",12),("b","A",76),("c","C",45),("d","B",36),("d","D",45)]
b=lambda x:x[2]>=18
#or
#def b(x):
#   return x[2]>=18
print(list(filter(b,a)))#only the function address
      
    
