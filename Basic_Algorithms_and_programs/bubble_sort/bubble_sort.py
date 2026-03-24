def bubble(lst):
    q=0
    while q!=(len(lst)-1):
        for a in range(len(lst) - 1):
            if lst[a]>lst[a+1]:
                lst[a],lst[a+1]=lst[a+1],lst[a]
                q=0
            else:
                q+=1
                if q==(len(lst)-1):
                    break
    print(lst)

bubble(eval(input("list")))
