from datetime import datetime
from pipes import Template
from pydoc import doc
from turtle import ht
from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
	return HttpResponse("Hola Django - Coder")
def miNombreEs(self, nombre):
	documentodetexto = f"Mi nombre es: <br><br> {nombre}"
	return HttpResponse(documentodetexto)
def edad(self, edad):
	anio  = datetime.now().year
	return HttpResponse(anio - int(edad))

def templaTest(self):
	nom = "fabri"
	listadenotas = [1,2,3,4,5]
	dicc = {"var1":nom, "hoy":datetime.now(), "lista1":listadenotas}
#   mihtml = open("c:/Users/JACK4/Documents/python coder/Proyecto1/Plantillas/template1.html")
#	m  = Template(mihtml.read())
#   mihtml.close()
#	contexto = Context(dicc)
#	documento = plantilla.render(contexto)

	plantilla = loader.get_template("template1.html")
	documento = plantilla.render(dicc)

	return HttpResponse(documento)
