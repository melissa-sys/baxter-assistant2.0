from django.shortcuts import render

from django.contrib.auth import authenticate, login

from django.http import HttpResponse

from django.views.generic import View
from django.views.generic import TemplateView


# Create your views here.
class LoginIndexView(TemplateView):
    template_name = 'login/login.html'
    redirect_field_name = 'redirect_to'

# def login_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return HttpResponse('Worked!')
#     else:
#         return HttpResponse('No funcionó')


# class LoginView
