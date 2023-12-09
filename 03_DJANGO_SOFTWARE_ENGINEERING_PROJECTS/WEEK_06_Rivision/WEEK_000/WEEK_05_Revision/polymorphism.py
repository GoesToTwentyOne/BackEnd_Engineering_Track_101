from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating shape instances
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)

# Using polymorphism to calculate areas
shapes = [circle, rectangle]

for shape in shapes:
    print(f"Area of {shape.__class__.__name__}: {shape.area()}")
    
    
    
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Creating animal instances
dog = Dog()
cat = Cat()
cow = Cow()

# Using polymorphism to make sounds
animals = [dog, cat, cow]

for animal in animals:
    print(f"The {animal.__class__.__name__} says: {animal.make_sound()}")
    
    
class Employee:
    def __init__(self, name):
        self.name = name

    def perform_task(self):
        pass

class Developer(Employee):
    def perform_task(self):
        return f"{self.name} is coding."

class Designer(Employee):
    def perform_task(self):
        return f"{self.name} is creating a design."

class Manager(Employee):
    def perform_task(self):
        return f"{self.name} is managing the team."

# Creating employee instances
john = Developer(name="John")
lisa = Designer(name="Lisa")
emma = Manager(name="Emma")

# Using polymorphism to perform tasks
employees = [john, lisa, emma]

for employee in employees:
    print(employee.perform_task())


