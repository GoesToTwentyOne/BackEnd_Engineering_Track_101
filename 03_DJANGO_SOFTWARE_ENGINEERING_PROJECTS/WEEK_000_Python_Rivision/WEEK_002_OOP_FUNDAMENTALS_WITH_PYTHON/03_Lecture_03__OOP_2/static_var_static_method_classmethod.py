class Person:
    cart=[]
    def __init__(self,age,id,name) -> None:
        self.age=age
        self.id=id
        self.name=name
    @classmethod
    def class_m(self,name,age):
        print(name,age)
    @staticmethod
    def static_m(name,age):
        print(name,age)
nihadgo75=Person(21,23,"Md. Nihad Hossain")
Person.class_m("Nihad",21)
nihadgo75.static_m("H",21)
Person.static_m("Nihad",21)
nihadgo75.class_m("Nihad",21)

    
        