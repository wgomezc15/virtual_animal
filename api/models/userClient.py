from django.db import models
from .typeDocument import TypeDocument
 
class UserClient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name',max_length=30)
    lastname = models.CharField('Lastname',max_length=30)
    email = models.EmailField('Email',max_length=100)
    typeDocument = models.ForeignKey(TypeDocument,related_name='userClienttypeDocument',on_delete=models.PROTECT)
    document = models.CharField('Document',max_length= 15,unique=True)
    telephone = models.CharField('Telephone',max_length=20)
    address = models.CharField('Address',max_length=100)
    gender = models.CharField('Gender',max_length=1)
    isActive = models.BooleanField(default=True)
    class Meta:
        ordering = ['id']
