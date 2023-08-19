from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25)
    roll=models.IntegerField(primary_key=True)
    address=models.TextField()
    address2=models.TextField(default="Dhaka")
    def __str__(self) -> str:
        return f" Roll: {self.roll} -- Name: {self.name} -- Address: {self.address}"
