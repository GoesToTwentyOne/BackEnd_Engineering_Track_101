from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='homepage'),
    path('delere/<int:roll>',views.delete_student,name="deleted_student"),
]
