from django.urls import path
from .import views 
urlpatterns = [
    path('',views.home,name="homepage"),
    path('signup/',views.signup,name="signup"),
    path('profile/',views.profile,name="profile"),
    path('login/',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('pass_change/',views.change_password,name="change_password"),
    path('password_change_set/',views.password_change_set,name="change_password_set"),
    path('change_user_data',views.change_user_data,name="change_user_data"),
]

