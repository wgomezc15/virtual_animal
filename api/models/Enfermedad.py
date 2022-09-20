from django.db import models

class tabla_Enfermedad(models.Model):
        id_Enfermedad = models.AutoField(primary_key=True)
        Nombre_Enfermedad = models.TextField('Enfermedad', max_length= 20, unique=True)
        Descripcion_Enfermedad = models.TextField('Descripciondeenfermedad', max_length= 200, unique=True)


