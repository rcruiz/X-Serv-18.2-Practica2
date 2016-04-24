from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from models import Url
import urllib


@csrf_exempt
def process(request, recurso):
    peticion = request.method
    cuerpo = request.body
    formulario = '<FORM action="" method="post"><p>'
    formulario += '<LABEL for="URL">URL: </LABEL>'
    formulario += '<INPUT type="text" name="url"><BR>'
    formulario += '<INPUT type="submit" value="Send"></p></FORM>'
    lURLs = Url.objects.all()
    if (peticion == "GET"):
        if recurso == "":
            respuesta = formulario + "<ul>"
            for url in lURLs:
                respuesta += "<li>" + url.urlLarga + " --> " + str(url.urlCorta) + "</li>"
            respuesta += "</ul>"
        else:
            if recurso.isdigit():
                try:
                    elemento = Url.objects.get(urlCorta=recurso)
                    respuesta = '<meta http-equiv="Refresh" content="3;url='
                    respuesta += elemento.urlLarga + '">'
                except Url.DoesNotExist:
                    respuesta = "Recurso no disponible"
            else:
                respuesta = "Recurso no valido"
    elif (peticion == "POST"):
        cuerpo = cuerpo.split('=')[1]
        cuerpo = urllib.unquote(cuerpo).decode('utf8')
        if cuerpo[0:4] != "http":  # Incluye http:// si es necesario
            cuerpo = "http://" + cuerpo
        try:
            elemento = Url.objects.get(urlLarga=cuerpo)
            respuesta = "Elemento ya almacenado</br>"
        except Url.DoesNotExist:  # Determina URL acortada
            numSec = len(lURLs)
            #urlCorta = str(numSec)
            elemento = Url(urlCorta=numSec, urlLarga=cuerpo)
            elemento.save()
            respuesta = "Elemento nuevo creado</br>"
        respuesta += '<a href="' + elemento.urlLarga + '">'
        respuesta += str(elemento.urlCorta) + '</a>'": "
        respuesta += '<a href="' + elemento.urlLarga + '">'
        respuesta += elemento.urlLarga + '</a>'
    return HttpResponse(respuesta)
