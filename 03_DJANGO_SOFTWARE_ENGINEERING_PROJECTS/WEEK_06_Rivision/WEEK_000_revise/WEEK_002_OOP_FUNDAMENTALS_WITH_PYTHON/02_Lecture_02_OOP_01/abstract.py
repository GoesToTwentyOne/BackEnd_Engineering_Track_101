from abc import ABC,abstractmethod
class Animal(ABC):
    
    def __init__(self,name) -> None:
        self.name=name
    @abstractmethod
    def eat(self):
        print("Need Food")
    @abstractmethod
    def move(self):
        print("running")
    def done(self):
        print("you are doing great")
class Monkey(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def eat(self):
        print("I need banana")
    def move(self):
        print("you are doing great")
yuri= Monkey("Youri")
print(yuri.name)
yuri.eat()
yuri.move()