class Soldier:
    def __init__(self,name,age,height) -> None:
        self.name = name
        self.age = age
        self.height = height
        
class BangladeshArmy(Soldier):
    def __init__(self,name,age,height,soldier_country) :
        self.soldier_country =soldier_country
        super().__init__(name,age,height)
    def __add__(self,other):
        return self.age + other.age
    def __mul__(self,other):
        return self.height * other.height
        


BanArmy1 =BangladeshArmy('Nihad0',25,50,'BD')
BanArmy2 =BangladeshArmy('Alex',20,55,'BD')
print(BanArmy1+BanArmy2) 
print(BanArmy1*BanArmy2) 

    