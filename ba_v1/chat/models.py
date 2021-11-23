from django.db import models
from jsonfield import JSONField

# Create your models here.


class Message(models.Model):
    message = JSONField(null=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    # se ejecuta cada que se ejecuta la instancia
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        # ordenaré los proyectos desde el más nuevo hasta el más antiguo. (-created)

    def __str__(self):
        # aquí me da el nombre del proyecto. Self es el contexto.
        return str(self.identifier)
