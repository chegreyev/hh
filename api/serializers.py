from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=100 , write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = ('id' , 'username' , 'password' , )

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    tags= serializers.StringRelatedField(many=True , read_only=True )

    def get_user(self , obj):
        return obj.user.username

    class Meta:
        model = Task
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['task' , 'name', ]
