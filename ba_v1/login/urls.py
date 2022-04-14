from django.urls import path, include

from . import views
from .views import LoginIndexView
from .views import BALoginView
from .views import BALogoutView
# from .views import login_view

app_name = 'login'
urlpatterns = [
    path('', BALoginView.as_view(), name='index'),
    path('logout', BALogoutView.as_view(), name='goodbye'),
    path('login', LoginIndexView.as_view(), name='home'),

]
