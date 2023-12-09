class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}   {self.price}"


class Bus(Vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self):
        return f"{self.seat}, {super().__repr__()}"


class Truck(Vehicle):
    def __init__(self, name, price, weight):
        self.weight = weight
        super().__init__(name, price)

    def __repr__(self):
        return f"{self.weight}, {super().__repr__()}"


class AcBus(Bus):
    def __init__(self, name, price, seat, temperature):
        self.temperature = temperature
        super().__init__(name, price, seat)

    def __repr__(self):
        return f"{self.temperature}, {super().__repr__()}"


class PickUp(Truck):
    def __init__(self, name, price, weight, lightWeightBody):
        self.lightWeightBody = lightWeightBody
        super().__init__(name, price, weight)

    def __repr__(self):
        return f"{self.lightWeightBody}  {super().__repr__()}"


BRTC = AcBus("BRTC", 53454545, 45, 23)
print(BRTC)

