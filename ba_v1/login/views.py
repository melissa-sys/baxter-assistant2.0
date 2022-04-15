from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin

from django.http import HttpResponseForbidden
from django.http import JsonResponse

from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


# Create your views here.
class LoginIndexView(TemplateView):
    template_name = 'login/login.html'
    redirect_field_name = 'redirect_to'

class BALoginView(SuccessMessageMixin, LoginView):
    template_name = 'login/login.html'

    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return redirect(reverse_lazy('chat:home'))
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        username = request.POST.get('user', None)
        password = request.POST.get('pass', None)
        print(username)
        print(password)

        if User.objects.filter(username=username).exists():
            User.objects.filter(username=username).update(password=password)
            u = User.objects.get(username=username)
            u.set_password(password)
            u.save()
            user = authenticate(
                username = username,
                password = password,
            )

            login(request,user)
            
            return redirect(reverse_lazy('chat:home'))
        else: 
            print ('entré')
            response = JsonResponse({"error":"Usuario no registrado, necesario para ingresar."})
            response.status_code = 403
            return response

        

    def get_success_message(self, cleaned_data):
        return '¡Bienvenido {}!'.format(self.request.user.username)

class BALogoutView(RedirectView):
    pattern_name = "login:index"

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)