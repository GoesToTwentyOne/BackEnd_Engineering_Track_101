from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import FormView,DeleteView,UpdateView
from to_do_app.forms import ToDoListForm
from to_do_app.models import ToDoListModel
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
class HomwView(TemplateView):
    template_name = 'home.html'

class Regester(FormView):
    template_name='register.html'
    form_class = ToDoListForm
    def form_valid(self, form):
        form.save(commit=True)
        return redirect('show_tasks')

class ShowTasksView(ListView):
    template_name='show_tasks.html'
    model=ToDoListModel
    context_object_name = 'tasks'

class DeleteTask(DeleteView):
    model=ToDoListModel
    template_name='confirmation.html'
    success_url = reverse_lazy('show_tasks')
class EditTask(UpdateView):
    model=ToDoListModel
    form_class=ToDoListForm
    template_name='register.html'
    success_url = reverse_lazy('show_tasks')
def complete_task(request, pk):
    task = get_object_or_404(ToDoListModel, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')
def DeleteCompleteTask(request, pk):
    task = get_object_or_404(ToDoListModel, pk=pk)
    if task.is_completed:
        task.delete()
    else:
        complete_task(request, pk)
    return redirect('show_tasks')


        
    

    
    
    
        
    
    