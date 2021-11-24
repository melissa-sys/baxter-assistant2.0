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


# class Chat(APIView):

#     def post(self, request):
#         i = 0
#         data = self.request.POST.get('json')
#         if data != None:
#             i += 1
#             print(data)
#             model = Message.objects.create(message=data, identifier=i)
#             print ("objeto creado")
#         return Response({'some': data})


class SetupBaxter(View):

    def post(self, request, *args, **kwargs):
        json = request.POST.get('accion', None)
        model = Message.objects.create(message=json)
        print(json)
        return HttpResponse('Success!')

    # Método para la eliminación de datos en la api


@api_view(['DELETE'])
def messageDelete(request):
    event = Message.objects.all()
    event.delete()

    return Response('deleted')


def receiveChatInfo(request):
    i = 0
    data = request.POST.get('json')
    data_intents = request.POST.get('json_intents')
    print('aquí está el json')

    if data is None:
        data_ent = None
    else:
        data_ent = json.loads(data)

    if data_intents is None:
        data_int = None
    else:
        data_int = json.loads(data_intents)

    # Creación de diccionario para envío a API
    dict_info = {}
    dict_info["intents"] = data_int
    dict_info["entities"] = data_ent

    print(dict_info)

    if data != None:
        model = Message.objects.create(message=dict_info)
        print("objeto creado")

    return redirect('chat:importante')


class Finish(TemplateView):
    template_name = 'chat/importante.html'
