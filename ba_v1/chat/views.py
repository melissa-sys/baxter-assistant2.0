#from _typeshed import Self
from django.shortcuts import redirect, render

from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

import json
from .models import Message

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class HomePage(TemplateView):
    template_name = 'chat/home.html'
    redirect_field_name = 'redirect_to'


class Finish(TemplateView):
    template_name = 'chat/importante.html'


class SetupBaxter(View):

    def post(self, request, *args, **kwargs):
        json = request.POST.get('accion', None)
        model = Message.objects.create(message=json)
        print(json)
        return HttpResponse(model)

# Procesamiento información desde el chatbot


def receiveChatInfo(request):
    i = 0
    #data = request.POST.get('json')
    data_generic = request.POST.get('json_generic')
    print('aquí está el json')

    # if data is None:
    #     data_ent = None
    # else:
    #     data_ent = json.loads(data)

    if data_generic is None:
        data_gen = None
    else:
        data_gen = json.loads(data_generic)

    # Creación de diccionario para envío a API
    dict_info = {}
    string_generic = data_gen[0]['text']

    if "Confirmando solicitud:" in string_generic:
        # Siempre existe una acción.
        # Acción
        start = string_generic.find("Acción: </b>") + 12
        end = string_generic.find("<br>", start)
        accion = string_generic[start:end]

        if "Parte" in string_generic:
            # Parte
            start = string_generic.find("Parte: </b>") + 12
            end = string_generic.find("<br>", start)
            parte = string_generic[start:end]
        else:
            parte = ""

        if "Objeto" in string_generic:
            # Objeto
            start = string_generic.find("Objeto: </b>") + 12
            end = string_generic.find("<br>", start)
            objeto = string_generic[start:end]
        else:
            objeto = ""

        if "Dirección" in string_generic:
            # Dirección
            start = string_generic.find("Dirección: </b>") + 16
            end = string_generic.find("<br>", start)
            direccion = string_generic[start:end]
        else:
            direccion = ""

        if "Posición" in string_generic:
            # Posición
            start = string_generic.find("Posición: </b>") + 14
            end = string_generic.find("<br>", start)
            posicion = string_generic[start:end]
        else:
            posicion = ""

        if "Cantidad de movimiento" in string_generic:
            # Cantidad movimientos
            start = string_generic.find("Cantidad de movimiento: </b>") + 29
            end = string_generic.find("<br>", start)
            movimiento = string_generic[start:end]
        else:
            movimiento = ""

        if "Articulación" in string_generic:
            start = string_generic.find("Articulación: </b>") + 20
            end = string_generic.find("<br>", start)
            articulacion = string_generic[start:end]
        else:
            articulacion = ""

        json_generic = {
            "accion": accion,
            "parte": parte,
            "objeto": objeto,
            "direccion": direccion,
            "posicion": posicion,
            "movimiento": movimiento,
            "articulacion": articulacion
        }

    else:
        json_generic = {}

    print(json_generic)

    if len(json_generic) != 0:
        model = Message.objects.create(message=json_generic)
        print("objeto creado")

    return redirect('chat:importante')

# Método para la eliminación de datos en la api


@api_view(['DELETE'])
def messageDelete(request):
    event = Message.objects.all()
    event.delete()

    return Response('deleted')
