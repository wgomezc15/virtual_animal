from django.db import models


class Tabla_Vacunas(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField('Name',max_length=20,unique=True)
    

