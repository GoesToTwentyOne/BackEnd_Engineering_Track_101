def fun(x,y,z,*args):
    print(args)
fun(2,3,4,5,6,6,6,6,6,6,6,6)

def funk(a,b,c,**args):
    print(a,b,c)
    print(args)
    for k,v in enumerate(args):
        print(k,v)
funk(H=32,L=45,Y=78,a=10,b=15,c=20)
