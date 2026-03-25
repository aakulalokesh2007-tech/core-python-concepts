def infix_to_postfix(ex):
    pr,st,ans,temp,pa=[["+","-"],["*","/","//"],["^"]],[],"",[],0
    for a in ex:
        if a.isalpha():
            ans+=a
        elif a in (pr[0]+pr[1]+pr[2]+["(",")"]):
            if len(st)!=0 or (pa!=0) or (a in ("(",")")):
                if (a in ("(",")")) or ((pa!=0)):
                    if a=="(":
                        pa+=1
                        temp.append([])
                    elif a==")":
                        while len(temp[pa-1])!=0:
                            ans+=temp[pa-1].pop()
                        temp.pop()
                        pa-=1
                    elif len(temp[pa-1])!=0 and ((a in pr[0]) or ((temp[pa-1][-1] in pr[1]) and (a in pr[1])) or (temp[pa-1][-1] in pr[2] and (a in pr[2]))) :
                        ans+=temp[pa-1].pop()
                        temp[pa-1]+=[a]
                    else:
                        temp[pa-1]+=[a]
                elif (((a in pr[0]) or ((st[-1] in pr[1]) and (a in pr[1])) or ((st[-1] in pr[2]) and (a in pr[2]))) and (pa==0)) :
                    ans+=st.pop()
                    st+=[a]
                else:
                    st+=[a]  
            else:
                st+=[a]
    while len(st)!=0:
        ans+=st.pop()
    return ans
qq="A*(B+(C+D)*(E+F)/G)*H"
print(infix_to_postfix(qq))


                        

                
                



