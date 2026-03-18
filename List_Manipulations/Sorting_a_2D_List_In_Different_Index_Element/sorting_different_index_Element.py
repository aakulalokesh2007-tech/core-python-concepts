a=[("a","F",12),("b","A",76),("c","C",45),("d","B",36),("d","D",45)]
def b(ab):
    return(ab[1])
    
#b=lambda ab:ab[1]
a.sort(key=b)

print(a)
