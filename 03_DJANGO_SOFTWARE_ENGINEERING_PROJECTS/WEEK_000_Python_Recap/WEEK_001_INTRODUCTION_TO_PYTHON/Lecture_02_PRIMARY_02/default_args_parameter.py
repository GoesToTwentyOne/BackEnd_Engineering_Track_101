def info(x,y,z=0,t=0):
    print(x,y,z,t)
info(3,4)
info(4,5,6)
info(5,6,7,4)



#*args
def all_good_numbers(x,y,*args):
    print(x,y)
    print(args)
    for i in args:
        print(i)

all_good_numbers(4,5,6,7,7,77,7,7,7,77,7,7,7,77,7,7,7,7,7,777,)