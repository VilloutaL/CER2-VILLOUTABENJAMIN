from typing import Any
from django.db import models
# Create your models here.
class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='photos')

    def __str__(self) -> str:
        return self.nombre

class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    detalle = models.CharField(max_length=200)
    detalle_corto = models.CharField(max_length=100)
    TIPO_CHOICES =(
        ("S","Suspension de actividades"),
        ("C","Suspension de clase"),
        ("I","informacion")
    )
    tipo = models.CharField(max_length=1, choices = TIPO_CHOICES)
    entidad =  models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.titulo