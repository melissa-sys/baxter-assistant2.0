# Realizar el CRUD del objeto

from rest_framework import viewsets

from .models import Message
from .serializer import ChatSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = ChatSerializer
