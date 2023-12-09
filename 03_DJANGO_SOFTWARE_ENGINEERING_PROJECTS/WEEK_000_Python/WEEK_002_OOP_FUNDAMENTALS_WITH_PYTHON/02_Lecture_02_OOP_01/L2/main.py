class Device:
    def __init__(self,brand,price,color,origin) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.origin=origin
    def run(self):
        return f"Running Well"
    

class Laptop(Device):
    def __init__(self,brand,price,color,origin,primary_memory,clock_speed,processor) -> None:
        self.primary_memory=primary_memory
        self.clock_speed=clock_speed
        self.processor=processor
        super().__init__(brand,price,color,origin)
    def codeing(self):
        return f"Laptop is good thing"
    

class Phone(Device):
    def __init__(self,brand,price,color,origin,camera,sim) -> None:
        self.camera=camera
        self.sim=sim
        super().__init__(brand,price,color,origin)
    def calling(self,number):
        return f"calling number {number}"
    def __repr__(self) -> str:
        return f"Phone features: {self.camera}      {self.sim}"
    

class Camera(Device):
    def __init__(self,brand,price,color,origin,lens,pixels) -> None:
        self.lens=lens
        self.pixels=pixels
        super().__init__(brand,price,color,origin)
    def changeLens(self):
        return f"change the lens"
    

my_phone= Phone("Samsung",120000,"black","USA","64 MP","Yes")
print(my_phone)

        

        

