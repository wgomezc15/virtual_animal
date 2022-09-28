from django.db import models
from .pet import Pet
 
class ConsultaMedica(models.Model):
    id = models.AutoField(primary_key=True)
    motivo = models.TextField('Motivo',null=False)
    fecha = models.DateField(null= False)
    peso = models.DecimalField(max_digits = 5,decimal_places = 2,null=False)
    ritmocardiaco = models.IntegerField(null=False)
    pet = models.ForeignKey(Pet,related_name='ConsultaPet',on_delete=models.PROTECT)
    isactive = models.BooleanField(default=True)

    class Meta:
        ordering = ['fecha']