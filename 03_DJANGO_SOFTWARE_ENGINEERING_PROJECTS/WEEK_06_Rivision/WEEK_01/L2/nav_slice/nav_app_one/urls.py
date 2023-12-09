from django.urls import path
from nav_app_one.views import one_home,one_contact,one_about
urlpatterns = [
    path('One_home/',one_home,name='One_home'),
    path('One_contact/',one_contact,name='One_contact'),
    path('One_about/',one_about,name='One_about'),
]
