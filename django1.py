import django
django.VERSION
django-admin startproject Proyecto1
print("test")

python manage.py runserver
python manage.py startapp MiAplicacion
python manage.py check MiAplicacion

python manage.py sqlmigrate MiAplicacion 0001
(Eso nos dará muchas líneas en código sql)

python manage.py makemigrations

 python manage.py migrate   
(Con ésto, esas líneas de sql impactan en nuestra base de datos)


from MiAplicacion.models import Curso
 curso = Curso(nombre="Python", camada=23800)
curso.save()