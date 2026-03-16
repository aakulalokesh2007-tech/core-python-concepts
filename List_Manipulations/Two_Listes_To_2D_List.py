def _2list_to_2dList(lname,lage):
    if len(lname)==len(lage):
        _2d=[(lname[a],lage[a]) for a in range (len(lage))]
        return(_2d)
    else:
        return "no matching length"

Lname=["narender", "jaya", "raju", "ramesh", "amit", "Piyush"]
Lage=[45,23,59,34,51,43]
list=_2list_to_2dList(Lname,Lage)
print(list)
