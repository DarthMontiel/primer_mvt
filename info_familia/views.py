from django.shortcuts import render
from info_familia.models import datos
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def vista_familia(reques):
    #Obtenemos los datos de la tabla
    familiares = datos.objects.all()

    #Diccionario de la lista familiares
    info = {"familiares":familiares}


    plantilla = loader.get_template("plantilla01.html")
    documento = plantilla.render(info)

    return HttpResponse(documento)
