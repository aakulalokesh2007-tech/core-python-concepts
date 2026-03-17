a=eval(input("your list"))
for b in range(len(a)):
    c=a[b]
    for d in (a[b:]):
        if c>d:
            c=d
    e=len(a[:b])
    for d in a[b:]:
        if d ==c:
            break
        e+=1
    a[b],a[e]=c,a[b]
print(a)
        
