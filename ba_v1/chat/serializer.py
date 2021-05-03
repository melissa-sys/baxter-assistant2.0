from rest_framework import serializers

from .models import Message

# Transportar el JSON


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
