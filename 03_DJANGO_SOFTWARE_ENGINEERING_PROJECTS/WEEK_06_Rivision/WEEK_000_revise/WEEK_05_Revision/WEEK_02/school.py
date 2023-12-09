class Student:
    def __init__(self,name,id,currentClass) -> None:
        self.name=name
        self.id=id
        self.currentClass=currentClass
    # def __repr__(self) -> str:
    #     return f"Student name is : {self.name},id : {self.id} and current class is :{ self.currentClass}"

class Teacher:
    def __init__(self,name,id,subject) -> None:
        self.name=name
        self.id=id,
        self.subject=subject
    # def __repr__(self) -> str:
    #     return f"Teacher name :{self.name},id :{self.id},subject : {self.subject}"


class School:

    def __init__(self,name) -> None:
        self.name=name
        self.teachers=[]
        self.students=[]
    def add_teacher(self,name,subject):
        id=len(self.teachers)+454545
        teacher=Teacher(name,id,subject)
        self.teachers.append(teacher)
   
    def add_student(self,name,current_class):
        id=len(self.students)+1011
        student=Student(name,id,current_class)
        self.students.append(student)



    def __repr__(self) -> str:
       
        print(f"Name of school {self.name}")
        for teacher in self.teachers:
            print(teacher)
        for student in self.students:
            print(student)
        return f"all done"
        
        
            
Royal=School("Royal Kindergarden")
Royal.add_student("A","Seven")
Royal.add_student("B","six")
Royal.add_student("C","eight")
Royal.add_student("D","nine")
Royal.add_student("E","six")
Royal.add_student("F","seven")
Royal.add_teacher("Tom Crus","Algo")
Royal.add_teacher("Tom Crus1","Science")
Royal.add_teacher("Tom Crus2","db")
Royal.add_teacher("Tom Crus3","Bio")
Royal.add_teacher("Tom Crus4","che")
Royal.add_teacher("Tom Crus5","cse")
Royal.add_teacher("Tom Crus6","me")
print(Royal)


        
       


