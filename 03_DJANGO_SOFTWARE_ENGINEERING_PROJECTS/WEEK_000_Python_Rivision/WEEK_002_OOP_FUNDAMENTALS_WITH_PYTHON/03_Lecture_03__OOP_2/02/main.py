class Shoping:
    cart=[]
    def __init__(self,name,loacation) -> None:
        self.name=name
        self.location=loacation
    @staticmethod
    def toBuy(item):
        print(f"{item}")
    @classmethod
    def toQuery(self,Price):
        print(Price)
#s1=Shoping("Jamuna","Dhaka")
Shoping.toQuery(4500)
Shoping.toBuy("T-Shirt")
        