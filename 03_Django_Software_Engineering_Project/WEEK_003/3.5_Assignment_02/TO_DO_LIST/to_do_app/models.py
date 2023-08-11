from django.db import models

# Create your models here.
class ToDoListModel(models.Model):
    taskTitle=models.CharField(max_length=100)
    taskDescription =models.TextField()
    is_completed=models.BooleanField(default=False)