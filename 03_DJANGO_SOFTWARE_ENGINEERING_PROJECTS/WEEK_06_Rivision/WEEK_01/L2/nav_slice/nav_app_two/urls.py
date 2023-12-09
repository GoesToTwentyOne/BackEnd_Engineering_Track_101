from django.urls import path
from nav_app_two.views import two_home,two_course
urlpatterns = [
    path('two_home/',two_home,name='two_home'),
    path('two_contact/',two_course,name='two_course'),
]