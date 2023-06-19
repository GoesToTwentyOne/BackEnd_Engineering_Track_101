def armysRank(rank1,rank2,**kargs):
    print(rank1,rank2)
    print(kargs)
    for i,value in kargs.items():
        print(i,value)
armysRank(rank2="Captain",rank1="Major",rank3="Cornel",rank4="Brigider Genaral",rank5="Major General",rank6="General")


def armyRank(*args,**kargs):
    print(args)
    print(kargs)
    for i in args:
        print(i)
    for i,v in kargs.items():
        print(i,v)
armyRank(1,2,3,4,5,8,6,rank2="Captain",rank1="Major",rank3="Cornel",rank4="Brigider Genaral",rank5="Major General",rank6="General")

def armyranksMulReturn(x,y,z):
    sum=x+y+z
    mul=x*y*z
    sub=x-y-z
    
    return sub, sum,sub

print(armyranksMulReturn(4,5,6))


def armyranksMulReturn2(x,y,z):
    sum=x+y+z
    mul=x*y*z
    sub=x-y-z
    
    return [sub, sum,sub]

print(armyranksMulReturn2(4,5,6))

