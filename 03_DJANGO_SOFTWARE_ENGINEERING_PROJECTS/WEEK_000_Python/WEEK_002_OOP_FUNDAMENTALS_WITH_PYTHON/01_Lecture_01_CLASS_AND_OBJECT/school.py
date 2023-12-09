class Student:
    def __init__(self,name,id,current_class) -> None:
        self.name=name
        self.id=id
        self.current_class=current_class
    def __repr__(self) -> str:
        return f"Student class Student Name {self.name},id {self.id}, current class {self.current_class}"
class Teacher:
    def __init__(self,name,id,subject) -> None:
        self.name=name
        self.id=id
        self.subject=subject
    def __repr__(self) -> str:
        return f"Teacher class Teacher Name {self.name},id {self.id}, subject  {self.subject}"
class School:
    def __init__(self,name) -> None:
        self.name=name
        self.student_cart=[]
        self.teacher_cart=[]
    def add_teacher(self,name,subject):
        id=len(self.teacher_cart)+1010
        teacher=Teacher(name,id,subject)
        self.teacher_cart.append(teacher)
    def add_student(self,name,admisson_fees):
        id=len(self.student_cart)+75750
        student=Student(name,id,"SWE Trac")
        self.student_cart.append(student)
    def __repr__(self) -> str:
        print(f"----------welcome to out school {self.name}----------")
        print(f"-------------------------Teacher list ----------------")
        for teacher in self.teacher_cart:
            print(teacher)
        print(f"-------------------------Student list ----------------")
        for student in self.student_cart:
            print(student)
        return f"done all process ,Now you are the school member"
    


        
    

# nihadgo75=Student("Md.Nihad Hossain",23,88)
# nihadgo75T=Teacher("Alex Goot",58,"Algo")
# print(nihadgo75)
# print(nihadgo75T)

nihadgo75=School("nihadgo75 Go learning")
nihadgo75.add_student("Alex",88)
nihadgo75.add_student("Tani",88)
nihadgo75.add_student("Sadi",88)
nihadgo75.add_student("Dudo",88)
nihadgo75.add_teacher("Todd","Algo")
nihadgo75.add_teacher("Todo","Golang")
nihadgo75.add_teacher("Hanif","C++")
nihadgo75.add_teacher("Guyo","AI Machanics")
print(nihadgo75)
        