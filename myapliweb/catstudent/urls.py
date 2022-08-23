 
from django.urls import path
from catstudent import views

 
urlpatterns = [
   path("", views.index, name="index"),
]