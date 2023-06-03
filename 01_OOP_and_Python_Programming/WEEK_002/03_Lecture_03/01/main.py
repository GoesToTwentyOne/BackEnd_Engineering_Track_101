class Person:
    def __init__(self,name,age,weight,height) -> None:
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
    def toSpeak(self):
        print("I'm human I'm taking to anyone,Ok!")
    def toWalk(self):
        raise NotImplementedError
class Cricketer(Person):
    def __init__(self, name, age, weight, height,team) -> None:
        self.team=team
        super().__init__(name, age, weight, height)
    def toSpeak(self):
        print("I'm  Sakib I'm taking to anyone,Ok!")
    def toWalk(self):
        print("I'm Sakib, I can walking any where")
    def __add__(self,other):
        return self.age + other.age
    def __mul__(self,other):
        return self.age * other.age

        


Sakib = Cricketer("Sakib",35,56,56,"Bangladesh")
Tamim = Cricketer("Sakib",35,56,56,"Bangladesh")
Musfiq = Cricketer("Sakib",35,56,56,"Bangladesh")

Mahmudullah = Cricketer("Sakib",35,56,56,"Bangladesh")
print(Sakib + Tamim)
print(Sakib * Tamim)
