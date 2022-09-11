from rest_framework import serializers
from api.models import User
from api.serializers.typeDocumentSerializer import TypeDocumentSerializer

class UserSerializer(serializers.ModelSerializer):
    
    #typeDocument = TypeDocumentSerializer()

    class Meta:
        model=User
        fields=['id','username','password','name','lastname','email','typeDocument','document','telephone','address','gender','isActive']
    
    def create(self, validated_data): 
        userInstance=User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj): 
        user = User.objects.get(id=obj.id)
        #typeDocument = TypeDocument.objects.get(id=user.typeDocument)
        return {
                'id':user.id,
                'username':user.username,
                'name':user.name,
                'lastname':user.lastname,
                'email':user.email,
                'typeDocument': {
                    "id":user.typeDocument.id,
                    "code":user.typeDocument.code,
                    "name":user.typeDocument.name
                },
                'document':user.document,
                'telephone':user.telephone,
                'address':user.address,
                'gender':user.gender,
                'isActive':user.isActive
                }