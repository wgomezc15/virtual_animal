from rest_framework import serializers
from api.models import User
from api.models import TypeDocument


#from authApp.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):
    typeDocument=TypeDocument()

    class Meta:
        model=User
        fields=['id','username','password','name','lastname','email','typeDocument','document','telephone','address','gender','isActive']
    
    def create(self, validated_data): 
        userInstance=User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj): 
        user=User.objects.get(id=obj.id)
        return{
            'id':user.id,
            'username':user.username,
            'password':user.password,
            'name':user.name,
            'lastname':user.lastname,
            'email':user.email,
            'typeDocument':user.typeDocument,
            'document':user.document,
            'telephone':user.telephone,
            'address':user.address,
            'gender':user.gender,
            'isActive':user.isActive

        }