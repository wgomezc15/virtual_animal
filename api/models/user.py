from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from .typeDocument import TypeDocument
 
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Los usuarios deben tener un nombre de usuario")
 
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, username, password):
        user = self.create_user(
            username = username,
            password = password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key = True)
    username = models.CharField('Username',max_length= 15,unique=True)
    password = models.CharField('Password',max_length=256)
    name = models.CharField('Name',max_length=30)
    lastname = models.CharField('Lastname',max_length=30)
    email = models.EmailField('Email',max_length=100)
    typedocument = models.ForeignKey(TypeDocument,related_name='typedocument',on_delete=models.PROTECT)
    document = models.CharField('Document',max_length= 15,unique=True)
    telephone = models.CharField('Telephone',max_length=20)
    address = models.CharField('Address',max_length=100)
    gender = models.CharField('Gender',max_length=1)
    isactive = models.BooleanField(default=True)
 
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
 
    objects = UserManager()
    USERNAME_FIELD = 'username'