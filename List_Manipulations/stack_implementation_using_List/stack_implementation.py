def push(stack,ele):
    if len(stack)==sc:
        print("overflow Error")
    else:
        stack.append(ele)
def pop(stack):
    if len(stack)==0:
        print("under flow")
    else:
        return stack.pop()
#main
sc=int(input("enter the stack capacity to be maintained:"))
li=[]

while True:
    print('''
          1. Push
          2.Pop
          any t break
        ''')
    val=int(input("enter your option"))
    if val==1:
        ele=int(input("enter your element:only numbers "))
        push(li,ele)
    elif val==2:
        pop(li)
    else :
        break

for x in li:print(x)