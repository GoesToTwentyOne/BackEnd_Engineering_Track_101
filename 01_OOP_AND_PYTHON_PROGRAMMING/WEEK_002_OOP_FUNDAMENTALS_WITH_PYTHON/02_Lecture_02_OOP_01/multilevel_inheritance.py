from cv2 import pencilSketch


class Grand_Father:
    def __init__(self,name,speak,car) -> None:
        self.name=name
        self.speak=speak
        self.car=car
    def Profession(self,profession_title):
        print(f"I'm a {profession_title}.")
    def House(self,number_of_flat):
        print(f"I have {number_of_flat} flat.")
    def workingExperience(self,experience):
        print(f"I worked with {experience}")
    def __repr__(self) -> str:
        print(f"Name {self.name},{self.speak},{self.car}")
        return ""
class Father(Grand_Father):
    def __init__(self, name, speak, car,bus,truck) -> None:
        self.bus=bus
        self.truck=truck
        super().__init__(name, speak, car)
    def Profession(self, profession_title):
        print(super().Profession(profession_title))
    def workingExperience(self, experience):
        print(super().workingExperience(experience))
    def House(self, number_of_flat):
         print(super().House(number_of_flat))
    def Research(self,reserches):
        print(f"{reserches}")
    def __repr__(self) -> str:
        parent_repr= super().__repr__()
        print(f"{parent_repr}\nAddition classificatoin {self.bus}, {self.truck}")
class Child(Father):
    def __init__(self, name, speak, car, bus, truck,helicopter) -> None:
        self.helicpter=helicopter
        super().__init__(name, speak, car, bus, truck)
    def Profession(self, profession_title):
        print(super().Profession(profession_title))
    def workingExperience(self, experience):
        print(super().workingExperience(experience))
    def House(self, number_of_flat):
         print(super().House(number_of_flat))
    def Expert(self,expert):
        print(f"{expert}")
    def __repr__(self) -> str:
        father_repr= super().__repr__()
        print(f"{father_repr}\nAditional {self.helicpter}")
        return ""
child= Child("Md. Niahd Hossain","English","Pajora","AC Volvo","Yes","Yes")
print(child)
        