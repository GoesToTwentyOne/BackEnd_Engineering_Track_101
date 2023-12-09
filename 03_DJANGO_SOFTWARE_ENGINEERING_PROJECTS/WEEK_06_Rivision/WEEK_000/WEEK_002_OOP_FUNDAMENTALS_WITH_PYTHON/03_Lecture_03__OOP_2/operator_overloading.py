class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def eat(self):
        print("Normal food")
    def toSpeak(self):
        print("Able to speak")
        raise NotImplementedError
class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)
    def eat(self):
        print("They Flow special diet plan for fitness")
    def toSpeak(self):
        print("Yes,English")
    
    #operator overloading
    def __add__(self,other):
        return self.age+other.age
    def __mul__(self,other):
        return self.age*other.age
    def __gt__(self,other):
        return self.age>other.age



Sakib= Cricketer("Shakib Al Hasan",31,6.3,56)

Musfiq= Cricketer("Musfiq",31,6.3,56)
Sakib.eat()
Sakib.toSpeak()
print(Sakib+Musfiq)
print(Sakib*Musfiq)
print(Sakib>Musfiq)