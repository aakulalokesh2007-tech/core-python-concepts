while True:
 n=(input("enter the number to check it is armsrong or enter to stop "))
 if n=='':
     break
 if n.isdigit:
  a=int(n)
  c=len(n)
  f=0

  while a!=0:
   e=a%10
   f+=e**c
   a//=10
  if f==int(n):
    print("The number" ,n,"is armstrong")
  else:
    print("the number " ,n,"is not armstrong")
 else:
    print("plz enter a valid number")

