#from _typeshed import Self
import os
from django.shortcuts import redirect

from django.http import HttpResponse

from django.views.generic import View
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

import json
from .models import Message

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.conf import settings

# Create your views here.


class HomePage(LoginRequiredMixin, TemplateView):
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
    data_generic = request.POST.get('json')
    print('aquí está el json')
    print(data_generic)
    print(type(data_generic))

    if data_generic is None:
        data_gen = None
    else:
        data_gen = json.loads(data_generic)

    print(type(data_gen))

    try:
        if data_gen['confirmacion'] == True:
            print(type(data_gen['confirmacion']))
            model = Message.objects.create(message=data_gen)
            print("objeto creado")
    except:
        pass

    return redirect('chat:importante')


def receiveOrdersInfo(request):
    i = 0
    #data = request.POST.get('json')
    data_generic = request.POST.get('accion')
    print('aquí está el json' + data_generic)

    context = {
        'accion': data_generic,
        'confirmacion': True
    }
    print(context)

    if len(context) != 0:
        model = Message.objects.create(message=context)
        print("objeto creado")

    return redirect('chat:importante')

# Método para la eliminación de datos en la api


@api_view(['DELETE'])
def messageDelete(request):
    event = Message.objects.all()
    event.delete()

    return Response('deleted')

# Módulo Voz
class Voice(TemplateView):

    template_name = 'chat/speech_text.html'

def datosRequest(request):
    path = os.path.dirname(os.path.join(settings.BASE_DIR, 'chat', 'static', 'dist'))
    file_name = 'datos.txt'
    datos = os.path.join(path,file_name)
    datos_usuario = open(datos, 'r')
    with datos_usuario as file:
        data = file.readlines()
        context = data        
        #return render(request,myapp/mytemplate.html,context)
        return HttpResponse(context)