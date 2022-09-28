from django.db import models
from .clientOwner import ClientOwner
 
class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name',max_length=30)
    age = models.IntegerField(default=0)
    race = models.CharField('Race',max_length=30)
    sex = models.CharField('Sex',max_length=1)
    species = models.CharField('Species',max_length=30)
    features = models.CharField('Features',max_length=30)
    isactive = models.BooleanField(default=True)
    client = models.ForeignKey(ClientOwner,related_name='petclient',on_delete=models.PROTECT)
    class Meta:
        ordering = ['id']