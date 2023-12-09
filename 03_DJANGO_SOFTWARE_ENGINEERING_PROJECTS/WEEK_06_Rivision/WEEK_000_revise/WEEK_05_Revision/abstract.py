from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}'s engine started.")

    def stop_engine(self):
        print(f"{self.make} {self.model}'s engine stopped.")

class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}'s engine started with a roar.")

    def stop_engine(self):
        print(f"{self.make} {self.model}'s engine stopped.")

# Creating vehicle instances
car = Car(make="Toyota", model="Camry")
motorcycle = Motorcycle(make="Harley-Davidson", model="Sportster")

# Starting and stopping engines
car.start_engine()
car.stop_engine()

motorcycle.start_engine()
motorcycle.stop_engine()
