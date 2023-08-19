from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from userapp.views import RegistrationView,LogoutView


urlpatterns = [
    path('login/',obtain_auth_token,name="login"),
    path('register/',RegistrationView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
]
