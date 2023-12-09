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

class Laptop:
    def __init__(self,ssd,mouse,keyboard,hipower_processor,ram) -> None:
        self.ssd=ssd
        self.mouse=mouse
        self.keyboard=keyboard
        self.hipower_processor=hipower_processor
        self.ram=ram
    def coding(self):
        print(f"Life chnging skill,in the modern days")

class Phone:
    def __init__(self,isSim,isMessage,easy_carry) -> None:
        self.isSim=isSim
        self.isMessage=isMessage
        self.easy_carry=easy_carry

    def textMessage(self):
        print(f"send a message {self.isMessage}")
    def dialCalling(self):
        print(f"dial calling applicable")

class Camera:
    def __init__(self,lens,pixel) -> None:
        self.lens=lens
        self.pixel=pixel

    
        
    


        