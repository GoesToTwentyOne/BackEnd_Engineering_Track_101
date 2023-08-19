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
