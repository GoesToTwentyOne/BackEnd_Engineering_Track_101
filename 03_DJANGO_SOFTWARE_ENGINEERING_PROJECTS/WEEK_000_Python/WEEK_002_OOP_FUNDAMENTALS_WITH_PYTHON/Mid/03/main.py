import math
class A:
    def __init__(self,a,b,c) -> None:
        self.a=a
        self.b=b
        self.c=c
    def sum(self):
        return self.a+self.b+self.c
    def factorial(self):
        return math.factorial(self.b)
    
ob1= A(10,3,30)
print(ob1.sum())
print(ob1.factorial())

        