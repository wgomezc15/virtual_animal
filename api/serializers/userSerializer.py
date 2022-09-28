from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['id','username','password','name','lastname','email','typedocument','document','telephone','address','gender','isactive']
    
    def create(self, validated_data): 
        userInstance=User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj): 
        user = User.objects.get(id=obj.id)
        return {
                'id':user.id,
                'username':user.username,
                'name':user.name,
                'lastname':user.lastname,
                'email':user.email,
                'typedocument': {
                    "id":user.typedocument.id,
                    "code":user.typedocument.code,
                    "name":user.typedocument.name
                },
                'document':user.document,
                'telephone':user.telephone,
                'address':user.address,
                'gender':user.gender,
                'isactive':user.isactive
                }