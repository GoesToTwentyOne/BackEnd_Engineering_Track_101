import dis


class Gadget:
    def __init__(self,brand,color,camera,price,display,varient) -> None:
        self.brand=brand
        self.color=color
        self.camera=camera
        self.price=price
        self.display=display
        self.varient=varient
    def run(self):
        print(f"every gadget help to world more faster and connected")
    def __repr__(self) -> str:
        print(f"Available features : {self.brand}, {self.camera}, {self.color}, {self.price}, {self.display}, {self.varient}")
        return ""

class Phone(Gadget):
    def __init__(self,isSim,isMessage,easy_carry,brand,color,camera,price,display,varient) -> None:
        self.isSim=isSim
        self.isMessage=isMessage
        self.easy_carry=easy_carry
        super().__init__(brand,color,camera,price,display,varient)

    def textMessage(self):
        print(f"send a message {self.isMessage}")
    def dialCalling(self):
        print(f"dial calling applicable")
    def __repr__(self):
        parent_repr = super().__repr__()  
        return f"{parent_repr}\nAdditional features: {self.isSim}, {self.isMessage}"
class Laptop(Gadget):
    def __init__(self,ssd,mouse,keyboard,hipower_processor,ram,brand,color,camera,price,display,varient) -> None:
        self.ssd=ssd
        self.mouse=mouse
        self.keyboard=keyboard
        self.hipower_processor=hipower_processor
        self.ram=ram
        super().__init__(brand,color,camera,price,display,varient)
    def coding(self):
        print(f"Life chnging skill,in the modern days")
    def __repr__(self) -> str:
        parent_repr= super().__repr__()
        print(f"{parent_repr}\n aditiontion features {self.ssd} ,{self.mouse} ,{self.keyboard} ,{self.hipower_processor}, {self.ram}")
        return " "

class Camera(Gadget):
    def __init__(self,lens,pixel,brand,color,camera,price,display,varient) -> None:
        self.lens=lens
        self.pixel=pixel
        super().__init__(brand,color,camera,price,display,varient)
    def __repr__(self) -> str:
        parent_repr= super().__repr__()
        print(f"{parent_repr}\nAditional Features: {self.lens} ,{self.pixel}")
        return " "


my_phone=Phone('Yes','Yes','Yes',"samsung","black","32 Mp",32000,"super amulate","Prime")
print(my_phone)
my_laptop= Laptop("128 Gb","Yes","Yes",'4.20 GHZ','32 GB',"ASUS","golden heart","32 MP","120000","Oleyed","K513 EA")
print(my_laptop)
my_camera=Camera('458F','7878787877',"ASUS","golden heart","32 MP","120000","Oleyed","K513 EA")
print(my_camera)


    
        
    


        