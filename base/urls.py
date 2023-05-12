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
    path('HeaderLogin/', views.headerlogin, name='HeaderLogin'),
    path('Header/', views.header, name='Header'),
    path('adminlogin/',views.login_viewadmin, name='adminlogin'),
    path('adminview/', views.admin_view, name='adminview'),
    path('homeloginadmin/', views.homeloginadmin, name='homeloginadmin'),
    path('headeradminlogin/', views.headeradminlogin, name='headeradminlogin'),
    path('mostrar_registros/', views.mostrar_registros, name='mostrar_registros'),
    path('eliminar_registro/<int:numero_edificio>/', views.eliminar_registro, name='eliminar_registro'),
    path('aceptar_registro/<int:numero_edificio>/', views.aceptar_registro, name='aceptar_registro'),

]