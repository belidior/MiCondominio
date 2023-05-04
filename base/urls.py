from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name='room'),
    path('base/', views.base, name='base'),
    path('login/', views.login_view, name='login'),
    path('homelogin/', views.homelogin, name='homelogin'),
    path('signup/', views.signup_view, name='signup'),
    path('Registro/', views.insertar_registro, name='Registro'),



]