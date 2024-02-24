from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model # If used custom user model
class TenthSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tenth
        fields='__all__'

class TwelfthSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Twelfth
        fields='__all__'

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.College
        fields='__all__'


class BasicDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BasicDetails
        fields='__all__'

class SchoolingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.SchoolingDetails
        fields='__all__'

class CollegeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CollegeDetails
        fields='__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Resume
        fields='__all__'
class UserListSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id', 'username','password', 'first_name', 'last_name')

UserModel = get_user_model()
class RegisteredUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            #gender=validated_data['gender'], if go Inside User model only username ,password,email,first_name ,last_name h isliye or koi aur field nhi lega
        )

        return user

    class Meta:
        model = UserModel

        fields = ( "id", "username", "password", "email","first_name","last_name") #( "id", "username", "password", "email","gender")
