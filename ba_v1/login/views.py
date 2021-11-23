from django.shortcuts import render

from django.contrib.auth import authenticate, login

from django.http import HttpResponse

from django.views.generic import View


# Create your views here.

# def login_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return HttoResponse('Worked!')
#     else:
#         return HttpResponse('No funcionó')


# class LoginView
