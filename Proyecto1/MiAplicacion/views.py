from datetime import datetime
from django.shortcuts import render, redirect
from MiAplicacion.models import Pariente, Curso, Tercera
from django.http import HttpResponse
from MiAplicacion.forms import Formulario

# Create your views here.

def alltables(request):
    miForm = Formulario()
    objs=Pariente.objects.all()  
    dictionario = {'objs':objs,'hoy':datetime.now(),"miForm":miForm,"objsdb":""}
    if request.method == 'POST': 
        miForm = Formulario(request.POST)

        print(miForm)
        if miForm.is_valid:
            info = miForm.cleaned_data
            curso = Curso (nombre = info['nombre'], camada = info['camada'])
            curso.save()
            e = datetime.now().strftime("%Y-%m-%d")
            tercera = Tercera(datochar = info["nombre"], datoint = info["camada"], datofecha = e)
            tercera.save()
            dictionario["forma"] = info
    if request.method == 'GET':
        camada = request.GET.get('camada', False)
        if camada == "":
            return render(request,'template2.html',dictionario)
        cursos = Curso.objects.filter(camada__icontains=camada)
        dictionario["cursos"] = cursos
        dictionario["camada"] = camada
        if len(cursos) == 0:
            dictionario["cursos"] = "placeholder"
    return render(request,'template2.html',dictionario)

def addpariente(self, stringg):
    lista = stringg.split("|")
    
    pariente = Pariente(nombre=lista[0], relacion=lista[1], fecha=lista[2])
    pariente.save()
    return redirect("http://127.0.0.1:8000/")

def delpariente(self, id):
    Pariente.objects.filter(id=id).delete()
    return redirect("http://127.0.0.1:8000/")
    
def verdb(request):
     objsdb=Curso.objects.all()  
    # return redirect("http://127.0.0.1:8000/", {"objsdb":objsdb})
     return render(request,'template3.html',{"objsdb":objsdb})