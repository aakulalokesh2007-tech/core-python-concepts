def gen(name,gender):
    if gender=='m':return ('MR.'+name)
    elif gender=='f':return ('MRS.'+name)
    else: return
print("welcome",gen(input("name"),input("gender 'm' for 'male' and 'f' 'female'"))) 
