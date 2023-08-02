from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('about/',views.about,name='about'),
    path('form/',views.submit_form,name="submit_form"),
    path('django_form/',views.django_form,name="django_form"),
    path('validation/',views.student_data,name="studentForm"),
    path('password',views.password,name="password"),
]
