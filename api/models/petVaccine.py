from django.db import models
from .pet import Pet
from .vaccines import Tabla_Vacunas

class PetVacinne(models.Model):
    id = models.AutoField(primary_key=True)
    pet = models.ForeignKey(Pet,related_name='vaccinepet',on_delete=models.PROTECT)
    vaccine = models.ForeignKey(Tabla_Vacunas,related_name='vaccinevaccine',on_delete=models.PROTECT)
    fecha = models.DateField()

    class Meta:
        ordering = ['fecha']