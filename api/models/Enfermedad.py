from pydoc import describe
from django.db import models


class Enfermedades (models.Model):

    class tabla_enfermedad(models.Model):
        id = models.AutoField(primary_key=True)
        id_Enfermedad = models.CharField(Enfermedad, max_length= 20)
        nombre =models.CharField(Enfermedad, max_length= 200)
        fecha_creacion = models.DateField("fecha_creacion",auto_now =False, auto_now_add=True)
        descripcion_Enfermedad = models.TextField()