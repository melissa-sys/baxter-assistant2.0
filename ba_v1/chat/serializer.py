from rest_framework import serializers

from .models import Message

# Transportar el JSON


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        # Asignación del modelo al serializador para posteo en API
        model = Message
        fields = '__all__'
