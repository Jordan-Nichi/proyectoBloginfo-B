from django.contrib import admin
from django.urls import path

from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
  
    path("", views.saludo, name= 'saludo'),
   
    path("despedir/", views.despedida, name= 'despedir'),
  
    path("nombre/", views.nombre, name= 'nombre'),
  

]
