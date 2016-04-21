from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Url

# Create your views here.
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
                respuesta += "<li>" + url.urlLarga + ": " + str(url.urlCorta) + "</li>"
            respuesta +=  "</ul>"
        else:
            if recurso.isdigit():
                urlCorta = int(recurso)

                try:
                    elemento = Url.objects.get(urlCorta = urlCorta)
                    respuesta = '<meta http-equiv="Refresh" content="5;url=' + elemento.urlLarga + '">'
                except Url.DoesNotExist:
                    respuesta = "Recurso no disponible"
            else:
                respuesta = "Recurso no valido"

    elif (peticion == "POST"):

            cuerpo = cuerpo.split('=')[1] 
            if cuerpo[0:7] != "http://":  # Incluye http:// si es necesario
                cuerpo = "http://" + cuerpo

            try:
                elemento = Url.objects.get(urlLarga = cuerpo)

            # Gestion de diccionarios con URL reales y acortadas
                numSec = elemento.urlCorta
                respuesta = "Elemento ya almacenado</br>"
                respuesta += '<a href="' + elemento.urlLarga + '">' + elemento.urlLarga + '</a>'
                respuesta += ": "
                respuesta += '<a href="' + elemento.urlLarga + '">' + str(elemento.urlCorta) + '</a>'
            except Url.DoesNotExist:  # Determina URL acortada
                numSec = len(lURLs)
                nuevoElemento = Url(urlCorta = numSec, urlLarga = cuerpo)
                nuevoElemento.save()
                respuesta = "Elemento nuevo creado</br>"
                respuesta += '<a href="' + nuevoElemento.urlLarga + '">' + nuevoElemento.urlLarga + '</a>'
                respuesta += ": "
                respuesta += '<a href="' + nuevoElemento.urlLarga + '">' + str(nuevoElemento.urlCorta) + '</a>'
    return HttpResponse(respuesta)
