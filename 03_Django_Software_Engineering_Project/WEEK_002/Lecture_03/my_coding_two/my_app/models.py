from django.db import models

# Create your models here.
class studentModel(models.Model):
    name=models.CharField(max_length=45)
    roll=models.IntegerField(primary_key=True)
    father_name=models.CharField(max_length=45)
    mother_name=models.CharField(max_length=45)
    address=models.TextField()


    def __str__(self) -> str:
        return f"{self.name}"
    

#abstract class inheritance test
class commonModel(models.Model):
    name=models.CharField(max_length=45)
    id=models.IntegerField(primary_key=True)
    address=models.TextField(max_length=50)
    class Meta:
        abstract=True
class studentInfoModel(commonModel):
    payment=models.IntegerField()
    section=models.CharField(max_length=45)
class teacherInfoModel(commonModel):
    subject=models.CharField(max_length=45)
    salary=models.IntegerField()

#multitable inheritance test 
class employeeModel(models.Model):
    name=models.CharField(max_length=45)
    id=models.IntegerField(primary_key=True)
    address=models.TextField(max_length=50)
    designation=models.CharField(max_length=44)
class managerModel(employeeModel):
    take_hire=models.BooleanField()
    take_interview=models.BooleanField()
    take_promotion=models.BooleanField()


# proxy model inheritance test
class FriendModel(models.Model):
    name = models.CharField(max_length=45)
    section = models.CharField(max_length=34)
    attendance = models.BooleanField()
    hw = models.CharField(max_length=50)

class MeModel(FriendModel):
    class Meta:
        proxy = True
        # ordering = ['id']


#one to one relationship
class Person(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    city=models.CharField(max_length=45)
    email=models.CharField(max_length=35)

    def __str__(self) -> str:
        return f"{self.name}"
class Passport(models.Model):
    person_user=models.OneToOneField(to="Person",on_delete=models.CASCADE,related_name='passport')
    passport_type=models.CharField(max_length=20)
    passport_number=models.IntegerField()
    page=models.IntegerField()
    validity=models.IntegerField()
    regional_office=models.CharField(max_length=45)

# one to many relationship
class Student(models.Model):
    name = models.CharField(max_length=45)
    id = models.IntegerField(primary_key=True)
    address = models.TextField(max_length=50)
    section = models.CharField(max_length=45)
    def __str__(self) -> str:
        return f"{self.name}"
class Library(models.Model):
    student_user=models.ForeignKey(to=Student, on_delete=models.SET_NULL,null=True)
    book_name=models.CharField(max_length=45)
    who_take_book=models.IntegerField()

# many to many relationship
# many to many relationship
class Studentinfo(models.Model):
    name=models.CharField(max_length=45)
    id =models.IntegerField(primary_key=True)
    address=models.TextField(max_length=50)
    cur_class=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
    def teacher_list(self):
        return ",".join([str(i) for i in self.teacherinfo.all()])
class Teacherinfo(models.Model):
    student_user=models.ManyToManyField(to=Studentinfo,related_name="teacherinfo")
    name=models.CharField(max_length=45)
    address=models.TextField(max_length=50)
    subject=models.CharField(max_length=45)
    salary=models.IntegerField()
    phone=models.CharField(max_length=11)
    def __str__(self) -> str:
        return f"{self.name}"

    def student_list(self):
        return ",".join([str(i) for i in self.student_user.all()])



