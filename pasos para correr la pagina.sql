pasos para instalar la pagina correctamente

1. pip install django
2. pip install cx_Oracle
3. Iniciamos servicios de oracle
4. Creamos usuario con los siguientes datos
	alter session set container = pdb;
	ALTER DATABASE OPEN;

	alter session set "_ORACLE_SCRIPT"=true;
	create user micondominio identified by 16511;
	grant connect,resource, unlimited tablespace to micondominio;

5. Luego de crear el usuario en oracle, ingresamos el siguiente comando python manage.py migrate
6. En el usuario creado de sql ingresamos la siguiente TABLA
	CREATE TABLE reservamicondominio (
	  NumeroEdificio INT PRIMARY KEY,
	  NombreResidente VARCHAR(50),
	  Area VARCHAR(10)
	);
7. ingresamos el siguiente comando python manage.py makemigrations
8. En settings y en el .views de la pagina cambiamos la direccion de la base de datos.
9. tiramos a andar la pagina con python manage.py runserver
