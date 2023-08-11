from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomwView.as_view(),name="homepage"),
    path('register/',views.Regester.as_view(),name="register"),
    path('show_tasks/',views.ShowTasksView.as_view(),name="show_tasks"),
    path('delete/<int:pk>',views.DeleteTask.as_view(),name="delete"),
    path('edit/<int:pk>',views.EditTask.as_view(),name="edit"),
    path('complete/<int:pk>',views.complete_task,name="complete"),
    path('completetaskdel/<int:pk>',views.DeleteCompleteTask,name="complete"),

]