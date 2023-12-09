class Student:
    def __init__(self, id,name,subject,present_class):
        self.id = id
        self.name = name
        self.present_class = present_class
        self.subject = subject
    def __repr__(self) -> str:
        return f"Student data , Name={self.name},Id={self.id} and PresentClass={self.present_class}"

class Teacher:
    def __init__(self,id,name,subject):
        self.id = id
        self.name = name
        self.subject = subject

class School:
    def __init__(self,school_EIN,School_name):
        self.school_EIN = school_EIN
        self.school_name =School_name
        self.students = []
        self.teachers = []
        
    def appoint_teacher(self,name,subject):
        id=len(self.teachers)+1010661
        teacher=Teacher(id,name,subject)
        self.teachers.append(teacher)
    
    def enroll_students(self,name,subject,present_class,fees):
        if fees >=4500:
            id=len(self.students)+1010551
            student=Student(id,name,subject,present_class)
            self.students.append(student)
    def teacher_view(self):
        for teacher in self.teachers:
            print(teacher)
            
    def student_view(self):
        for student in self.students:
            print(student)
            
    def __repr__(self):
       
        print(f"-------------------------> Our School --------------------->")
        print(f"{self.school_EIN} and {self.school_name}")
        print(f"-------------------------> Our Teacher --------------------->")
        print(f"{self.teacher_view()}")
        print(f"-------------------------> Our Student --------------------->")
        print(f"{self.student_view()}")
        return""
        

    
    
cant_saidpur=School(444444444,"Cant. Public Saidpur")
cant_saidpur.enroll_students("Nihad","ALgorithm",15,8000)
cant_saidpur.enroll_students("Alex","Database",15,7000)
cant_saidpur.enroll_students("Nabila","SQL",15,5000)
cant_saidpur.enroll_students("Oishi","ALgorithm",15,8000)
cant_saidpur.appoint_teacher("Tom Curs","ALgorithm")
cant_saidpur.appoint_teacher("Tom Alex","DSA")
cant_saidpur.appoint_teacher("Tom Don","Database")
cant_saidpur.appoint_teacher("Tom Sanmi","SQL")
cant_saidpur.appoint_teacher("Tom Biijj","ALgorithm")
print(cant_saidpur)

        
        
        
        