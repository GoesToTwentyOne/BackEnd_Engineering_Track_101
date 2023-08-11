from django import forms
from to_do_app.models import ToDoListModel

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoListModel
        fields = ['taskTitle','taskDescription']