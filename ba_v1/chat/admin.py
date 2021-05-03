from django.contrib import admin
from .models import Message

# Register your models here.

# Register your models here.
# Extenderé las funcionalizades del panel de administración


class MessagetAdmin(admin.ModelAdmin):
    # mostrará los campos como solo lectura
    readonly_fields = ('created', 'updated')


# Aquí importé el modelo que creé antes.
admin.site.register(Message, MessagetAdmin)
