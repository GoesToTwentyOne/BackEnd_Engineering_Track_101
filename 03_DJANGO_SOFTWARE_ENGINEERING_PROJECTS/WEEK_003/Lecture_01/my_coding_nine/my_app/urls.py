from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('get/',views.get_cookies,name='get_cookies'),
    path('del/',views.delete_cookies,name='delete_cookies'),
    path('set_session/',views.set_session,name='set_sesstion'),
    path('get_session/',views.get_sessions,name='get_sessions'),
    path('del_session/',views.delete_session,name='del_session'),
    path('ex_session/',views.session_expired,name='session_expired'),
]
