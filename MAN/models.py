from django.db import models

class Mascota(models.Model):

    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=60)
    imagen = models.URLField(max_length=500)

    def __str__(self):
        return '['+ str(self.codigo) +'] '+self.nombre
