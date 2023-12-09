class pen:
    writeing_lenght=.6
    def __init__(self,brand,nib_size,head,data):
        self.brand=brand
        self.nib_size=nib_size
        self.head=head
        self.data=data
    def ShowPrint(self):
        return("I'm from pen class")
p1= pen(brand="martador",nib_size=4.5,head="round-thinker",data=["Bangladesh","India","China"])
p2= pen(brand="Apex",nib_size=5.5,head="round-thinner",data=["Bangladesh","India","China"])
p3= pen(brand="All-Time",nib_size=3.5,head="round-bold",data=["Bangladesh","India","China"])
print(p1.brand,p1.writeing_lenght,p1.nib_size,p1.head,p1.data,p1.ShowPrint())
print(p2.brand,p2.writeing_lenght,p2.nib_size,p2.head,p2.data,p2.ShowPrint())
print(p3.brand,p3.writeing_lenght,p3.nib_size,p3.head,p3.data,p3.ShowPrint())



