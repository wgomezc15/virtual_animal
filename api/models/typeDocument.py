from django.db import models
 
class TypeDocument(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField('Code',max_length=4, unique=True)
    name = models.CharField('Name',max_length=20,unique=True)
    class Meta:
        ordering = ['id']