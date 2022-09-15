from django.db import models
from .pet import Pet #esperando al modelo y clase pet

class AnimalVaccinations(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField('Name', max_length=60)
    idPet=models.ForeignKey(Pet, related_name='petID',on_delete=models.PROTECT)

