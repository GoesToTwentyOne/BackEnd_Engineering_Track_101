class CPU:
    def __init__(self,core,clock_speed) -> None:
        self.core=core
        self.clock_speed=clock_speed
    def __repr__(self) -> str:
        print(f'{self.core}  {self.clock_speed}')
        return ""
class RAM:
    def __init__(self,version) -> None:
        self.version=version
    def __repr__(self) -> str:
        print(f"{self.version}")
        return ""
class SSD:
    def __init__(self,capacity) -> None:
        self.capacity=capacity
    def __repr__(self) -> str:
        print(f"{self.capacity}")
        return " "
    

class COMPUTER:
    def __init__(self,core,clock_speed,version,capacity) -> None:
        self.cpu=CPU(core,clock_speed)
        self.ram=RAM(version)
        self.ssd=SSD(128)

    def __repr__(self) -> str:
        self.cpu.__repr__()
        self.ram.__repr__()
        self.ssd.__repr__()
        return " "
computer=COMPUTER(8,32589898,"DDR5",'512GB')
print(computer)
        
        