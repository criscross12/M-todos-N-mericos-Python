from django.urls import path
from App_Web import views 

urlpatterns = [
    path('biseccion',views.Home, name='Home'),
    path('derivacion',views.derivada, name='derivada'),
    path('Home',views.home, name='home'),
    path('Integracion',views.interger, name='Integraci'),
    path('Euler',views.Euler, name='Euler'),

]