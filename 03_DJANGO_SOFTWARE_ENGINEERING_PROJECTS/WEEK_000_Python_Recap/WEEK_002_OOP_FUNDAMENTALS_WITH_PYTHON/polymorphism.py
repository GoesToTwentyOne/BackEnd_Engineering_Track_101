
class Animal:
    def __init__(self,name) -> None:
        self.name=name
    def make_sound(self):
        print("I'm animal")
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("mew mew")
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("gew gew")
class Cook(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("cook cook")
cat = Cat("Heyna")
cat.make_sound()
dog = Dog("Heyna")
dog.make_sound()
cook = Cook("Heyna")
cook.make_sound()





class Shape:
    def __init__(self,width,height) -> None:
        self.width=width
        self.height=height
    def area(self):
        print("i'm from parent class")
class Tringle(Shape):
    def __init__(self, width, height) -> None:
        super().__init__(width, height)
    def area(self):
        print(f"Triangle area is : {0.5* self.height * self.width}")
class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        super().__init__(width, height)
    def area(self):
        print(f"Rectangle area is : {self.height * self.width}")
class circle(Shape):
    def __init__(self, width, height) -> None:
        super().__init__(width, height)
    def area(self):
        print(f"Circle area is : {self.height * self.height*3.1416}")
tringle = Tringle(4,5)
tringle.area()
rectangle = Rectangle(4,5)
rectangle.area()
        

