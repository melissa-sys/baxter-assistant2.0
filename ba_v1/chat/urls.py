from django.urls import path, include

from . import views
from .views import HomePage
from .views import Chat
from .viewset import MessageViewSet

from rest_framework import routers

router = routers.SimpleRouter()  # Me da las rutas
router.register('message', MessageViewSet)

app_name = 'chat'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('send/', Chat.as_view(), name='send'),
    path('api/', include(router.urls), name='api'),
]
