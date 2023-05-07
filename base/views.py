from django.shortcuts import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import reservamicondominio
import cx_Oracle
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


# Create your views here.
#######################################################################################################
def home(request):
    return render(request, 'home.html')
def room(request):
    return render(request, 'room.html')
def base(request):
    return render(request, 'base.html')
def homelogin(request):
    return render(request, 'homelogin.html')
def Registro(request):
    return render(request,'Registro.html')
def headerlogin(request):
    return render(request,'headerlogin.html')
def header(request):
    return render(request,'header.html')
def admin_view(request):
    return render(request, 'admin.html')
def homeloginadmin(request):
    return render(request, 'homeloginadmin.html')
def headeradminlogin(request):
    return render(request, 'headeradminlogin.html')
#######################################################################################################
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            return redirect('homelogin')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#######################################################################################################
def login_viewadmin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('headeradminlogin')
            else:
                messages.error(request, 'Acceso denegado. Solo el administrador puede iniciar sesión.')
                return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'admin.html', {'form': form})

#######################################################################################################
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log in the user
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
#######################################################################################################
def insertar_registro(request):
    if request.method == 'POST':
        form = reservamicondominio(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            try:
                conexion = cx_Oracle.connect('micondominio/16511@127.0.0.1:1521/xe')
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO reservamicondominio(NumeroEdificio, NombreResidente, Area) VALUES (:1, :2, :3)", [datos['NumeroEdificio'], datos['NombreResidente'], datos['Area']])
                conexion.commit()
                mensaje = "Solicitud enviada correctamente, le llegara una noticicacion a su correo en caso de ser aprobada"
            except Exception as e:
                mensaje = "Error al insertar registro: " + str(e)
            finally:
                cursor.close()
                conexion.close()
    else:
        form = reservamicondominio()
        mensaje = None
    return render(request, 'Registro.html', {'form': form, 'mensaje': mensaje})
#######################################################################################################
def mostrar_registros(request):
    reservamicondominio = reservamicondominio.objects.all()
    return render(request, 'mostrar_registros.html', {'reservamicondominio': reservamicondominio})