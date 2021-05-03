from django.shortcuts import render

from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import json

from .models import Message

# from rest_framework.views import APIView
# from rest_framework.response import Response

from django.views.generic import TemplateView

# Create your views here.


class HomePage(TemplateView):
    template_name = 'chat/home1.html'


class Chat(TemplateView):

    template_name = 'chat/chatbot.html'

    def post(self, request):
        i = 0
        data = self.request.POST.get('json')
        if data != None:
            i += 1
            print(data)
            model = Message.objects.create(message=data, identifier=i)
            print ("objeto creado")
        return HttpResponseRedirect(reverse_lazy('chat:send'))

# class MyOwnView(APIView):
#     def get(self, request):
#         return Response({'some': 'data'})
