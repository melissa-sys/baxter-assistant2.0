from django.urls import path, include

from . import views
from .views import LoginIndexView
# from .views import login_view

app_name = 'login'
urlpatterns = [
    path('', LoginIndexView.as_view(), name='home'),

]
