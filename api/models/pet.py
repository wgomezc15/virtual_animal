from django.db import models
from .userClient import UserClient
 
class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name',max_length=30)
    age = models.IntegerField(default=0)
    race = models.CharField('Race',max_length=30)
    sex = models.CharField('Sex',max_length=1)
    species = models.CharField('Species',max_length=30)
    features = models.CharField('Features',max_length=30)
    isActive = models.BooleanField(default=True)
    userClient = models.ForeignKey(UserClient,related_name='PetuserClient',on_delete=models.PROTECT)
    class Meta:
        ordering = ['id']