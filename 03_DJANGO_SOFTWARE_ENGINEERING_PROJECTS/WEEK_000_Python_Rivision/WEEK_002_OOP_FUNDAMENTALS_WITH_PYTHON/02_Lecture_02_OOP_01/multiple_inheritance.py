class Family:
    def __init__(self,address) -> None:
        self.address=address
    def __repr__(self) -> str:
        print(f"Family address : {self.address}")
        return ""
class School:
    def __init__(self,id,level) -> None:
        self.id=id
        self.level=level
    def __repr__(self) -> str:
        print(f"school {self.id} , {self.level}")
        return ""
class Sports:
    def __init__(self,game) -> None:
        self.game=game
    def __repr__(self) -> str:
        print(f"Sports {self.game}")

        return ""
class Student(Family,School,Sports):
    def __init__(self, address,id,level,game,student) -> None:
        self.student=student
        School.__init__(self,id,level)
        Sports.__init__(self,game)
        Family.__init__(self,address)
    def __repr__(self) -> str:
        print(f"{Family.__repr__(self)},{School.__repr__(self)},{Sports.__repr__(self)},{self.student}")
        return ""
nihadgo75=Student("Bangladesh",23,2,"Footbal",'Yes')
print(nihadgo75)
        
        
        