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
                cursor.execute("INSERT INTO reservamicondominio(NumeroEdificio, NombreResidente, Area, FechaEstimada) VALUES (:1, :2, :3, :4)", [datos['NumeroEdificio'], datos['NombreResidente'], datos['Area'], datos['FechaEstimada']])
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
    try:
        mensaje = ""
        conexion = cx_Oracle.connect('micondominio/16511@127.0.0.1:1521/xe')
        cursor = conexion.cursor()
        cursor.execute("SELECT NumeroEdificio, NombreResidente, Area, FechaEstimada FROM reservamicondominio")
        registros = cursor.fetchall()
    except Exception as e:
        registros = None
        mensaje = "Error al obtener registros: " + str(e)
    finally:
        cursor.close()
        conexion.close()
    return render(request, 'mostrar_registros.html', {'registros': registros, 'mensaje': mensaje})
#######################################################################################################
def eliminar_registro(request, numero_edificio):
    try:
        conexion = cx_Oracle.connect('micondominio/16511@127.0.0.1:1521/xe')
        cursor = conexion.cursor()
        
        # Obtén los datos del registro que deseas mover
        cursor.execute("SELECT * FROM reservamicondominio WHERE NumeroEdificio = :1", [numero_edificio])
        datos_registro = cursor.fetchone()
        
        if datos_registro:
            # Inserta los datos en la otra tabla
            cursor.execute("INSERT INTO reservarechazada(NumeroEdificio, NombreResidente, Area, FechaEstimada) VALUES (:1, :2, :3, :4)", datos_registro)
            
            # Elimina el registro de la tabla original
            cursor.execute("DELETE FROM reservamicondominio WHERE NumeroEdificio = :1", [numero_edificio])
            conexion.commit()
            
            mensaje = "Registro rechazado correctamente"
        else:
            mensaje = "No se encontró el registro"
            
    except Exception as e:
        mensaje = "Error al mover registro: " + str(e)
        
    finally:
        cursor.close()
        conexion.close()
        
    return redirect('mostrar_registros')
#######################################################################################################
def aceptar_registro(request, numero_edificio):
    try:
        conexion = cx_Oracle.connect('micondominio/16511@127.0.0.1:1521/xe')
        cursor = conexion.cursor()
        
        # Obtén los datos del registro que deseas mover
        cursor.execute("SELECT * FROM reservamicondominio WHERE NumeroEdificio = :1", [numero_edificio])
        datos_registro = cursor.fetchone()
        
        if datos_registro:
            # Inserta los datos en la otra tabla
            cursor.execute("INSERT INTO reservaaceptada(NumeroEdificio, NombreResidente, Area, FechaEstimada) VALUES (:1, :2, :3, :4)", datos_registro)
            
            # Elimina el registro de la tabla original
            cursor.execute("DELETE FROM reservamicondominio WHERE NumeroEdificio = :1", [numero_edificio])
            conexion.commit()
            
            mensaje = "Registro aceptada correctamente"
        else:
            mensaje = "No se encontró el registro"
            
    except Exception as e:
        mensaje = "Error al mover registro: " + str(e)
        
    finally:
        cursor.close()
        conexion.close()
        
    return redirect('mostrar_registros')


