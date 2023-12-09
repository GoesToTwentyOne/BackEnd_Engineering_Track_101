from django.urls import path
from . import views
urlpatterns = [
    path('A/',views.a),
    path('B/',views.b),
]
