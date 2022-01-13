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
    data_generic = request.POST.get('json')
    print('aquí está el json')
    print(data_generic)

    if data_generic is None:
        data_gen = None
    else:
        data_gen = json.loads(data_generic)

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
        'accion': data_generic
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
