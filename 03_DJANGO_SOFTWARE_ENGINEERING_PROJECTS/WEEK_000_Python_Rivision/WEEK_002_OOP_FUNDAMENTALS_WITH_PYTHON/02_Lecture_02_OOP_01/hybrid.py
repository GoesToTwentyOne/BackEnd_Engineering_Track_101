class Grand_Father:
    def __init__(self, name, speak, car):
        self.name = name
        self.speak = speak
        self.car = car

    def Profession(self, profession_title):
        print(f"I'm a {profession_title}.")

    def House(self, number_of_flat):
        print(f"I have {number_of_flat} flat.")

    def workingExperience(self, experience):
        print(f"I worked with {experience}")

    def __repr__(self):
        return f"Name {self.name}, {self.speak}, {self.car}"


class Father(Grand_Father):
    def __init__(self, name, speak, car, bus, truck):
        self.bus = bus
        self.truck = truck
        super().__init__(name, speak, car)

    def Profession(self, profession_title):
        super().Profession(profession_title)

    def workingExperience(self, experience):
        super().workingExperience(experience)

    def House(self, number_of_flat):
        super().House(number_of_flat)

    def Research(self, reserches):
        print(f"{reserches}")

    def __repr__(self):
        parent_repr = super().__repr__()
        return f"{parent_repr}\nAdditional classification {self.bus}, {self.truck}"


class Child(Father):
    def __init__(self, name, speak, car, bus, truck, helicopter):
        self.helicpter = helicopter
        super().__init__(name, speak, car, bus, truck)

    def Profession(self, profession_title):
        super().Profession(profession_title)

    def workingExperience(self, experience):
        super().workingExperience(experience)

    def House(self, number_of_flat):
        super().House(number_of_flat)

    def Expert(self, expert):
        print(f"{expert}")

    def __repr__(self):
        father_repr = super().__repr__()
        return f"{father_repr}\nAdditional {self.helicpter}"


class Nihad(Father, Grand_Father):
    def __init__(self, name, speak, car, bus, truck, yut):
        self.yut = yut
        super().__init__(name, speak, car, bus, truck)

    def __repr__(self):
        father_repr = super().__repr__()
        return f"{father_repr}\nAdditional {self.yut}"


niahdgo75 = Nihad("Md. Nihad Hossain", "English", "Pajora", "AC Volvo", "Yes", "Yes")
print(niahdgo75)
